import logging
from typing import Literal, Sequence

from hhd.controller import Event
from hhd.controller.base import RgbMode
from hhd.controller.lib.hid import Device
import time

from .const import (
    COMMANDS_GAME,
    COMMANDS_MOUSE,
    RGB_APPLY,
    RGB_INIT_1,
    RGB_INIT_2,
    RGB_SET,
    buf,
)

Zone = Literal["all", "left_left", "left_right", "right_left", "right_right"]
GamepadMode = Literal["default", "mouse", "macro"]
Brightness = Literal["off", "low", "medium", "high"]

logger = logging.getLogger(__name__)


def rgb_set_brightness(brightness: Brightness):
    match brightness:
        case "high":
            c = 0x03
        case "medium":
            c = 0x02
        case "low":
            c = 0x01
        case _:
            c = 0x00
    return buf([0x5A, 0xBA, 0xC5, 0xC4, c])


def rgb_command(
    zone: Zone,
    mode: RgbMode,
    direction,
    speed: str,
    red: int,
    green: int,
    blue: int,
    o_red: int,
    o_green: int,
    o_blue: int,
):
    c_direction = 0x00
    set_speed = True

    match mode:
        case "solid":
            # Static
            c_mode = 0x00
            set_speed = False
        case "pulse":
            # Strobing
            # c_mode = 0x0A
            # Spiral is agressive
            # Use breathing instead
            # Breathing
            c_mode = 0x01
            o_red = 0
            o_green = 0
            o_blue = 0
        case "rainbow":
            # Color cycle
            c_mode = 0x02
        case "spiral":
            # Wave
            c_mode = 0x03
            red = 255
            green = 255
            blue = 255
            if direction == "left":
                c_direction = 0x01
        case "duality":
            # Breathing
            c_mode = 0x01
        # case "direct":
        #     # Direct/Aura
        #     c_mode = 0xFF
        # Should be used for dualsense emulation/ambilight stuffs
        case _:
            c_mode = 0x00

    c_speed = 0xE1
    if set_speed:
        match speed:
            case "low":
                c_speed = 0xE1
            case "medium":
                c_speed = 0xEB
            case _:  # "high"
                c_speed = 0xF5

    match zone:
        case "left_left":
            c_zone = 0x01
        case "left_right":
            c_zone = 0x02
        case "right_left":
            c_zone = 0x03
        case "right_right":
            c_zone = 0x04
        case _:
            c_zone = 0x00

    return buf(
        [
            0x5A,
            0xB3,
            c_zone,  # zone
            c_mode,  # mode
            red,
            green,
            blue,
            c_speed if mode != "solid" else 0x00,
            c_direction,
            0x00,  # breathing
            o_red,  # these only affect the breathing mode
            o_green,
            o_blue,
        ]
    )


def rgb_set(
    side: str,
    mode: RgbMode,
    direction: str,
    speed: str,
    red: int,
    green: int,
    blue: int,
    red2: int,
    green2: int,
    blue2: int,
):
    match side:
        case "left_left" | "left_right" | "right_left" | "right_right":
            return [
                rgb_command(
                    side, mode, direction, speed, red, green, blue, red2, green2, blue2
                ),
            ]
        case "left":
            return [
                rgb_command(
                    "left_left",
                    mode,
                    direction,
                    speed,
                    red,
                    green,
                    blue,
                    red2,
                    green2,
                    blue2,
                ),
                rgb_command(
                    "left_right",
                    mode,
                    direction,
                    speed,
                    red,
                    green,
                    blue,
                    red2,
                    green2,
                    blue2,
                ),
            ]
        case "right":
            return [
                rgb_command(
                    "right_right",
                    mode,
                    direction,
                    speed,
                    red,
                    green,
                    blue,
                    red2,
                    green2,
                    blue2,
                ),
                rgb_command(
                    "right_left",
                    mode,
                    direction,
                    speed,
                    red,
                    green,
                    blue,
                    red2,
                    green2,
                    blue2,
                ),
            ]
        case _:
            return [
                rgb_command(
                    "all", mode, direction, speed, red, green, blue, red2, green2, blue2
                ),
            ]


INIT_EVERY_S = 10


def process_events(events: Sequence[Event], prev_mode: str | None):
    cmds = []
    mode = None
    br_cmd = None
    init = False
    for ev in events:
        if ev["type"] == "led":
            if ev["initialize"]:
                init = True
            if ev["mode"] == "disabled":
                mode = "disabled"
                br_cmd = rgb_set_brightness("off")
                # cmds.extend(rgb_set(ev["code"], "solid", "left", 0, 0, 0, 0))
            else:
                match ev["mode"]:
                    case "pulse":
                        mode = "pulse"
                        set_level = False
                    case "rainbow":
                        mode = "rainbow"
                        set_level = False
                    case "duality":
                        mode = "duality"
                        set_level = False
                    case "solid":
                        mode = "solid"
                        set_level = True
                    case "spiral":
                        mode = "spiral"
                        set_level = True
                    case _:
                        assert False, f"Mode '{ev['mode']}' not supported."

                if set_level:
                    br_cmd = rgb_set_brightness(ev["brightnessd"])

                cmds.extend(
                    rgb_set(
                        ev["code"],
                        mode,
                        ev["direction"],
                        ev["speedd"],
                        ev["red"],
                        ev["green"],
                        ev["blue"],
                        ev["red2"],
                        ev["green2"],
                        ev["blue2"],
                    )
                )

    if not mode or (not cmds and mode != "disabled"):
        # Avoid sending init commands without a mode.
        # The exception being the disabled mode, which just sets the led
        # brightness.
        return [], None

    # Set brightness once per update
    if mode != prev_mode:
        init = True
        if not br_cmd:
            br_cmd = rgb_set_brightness("high")

    if init:
        cmds = [
            RGB_INIT_1,
            RGB_INIT_2,
            *cmds,
            RGB_SET,
            RGB_APPLY,
        ]

    if br_cmd:
        cmds.insert(0, br_cmd)
    return cmds, mode


class RgbCallback:
    def __init__(self) -> None:
        self.prev_mode = None

    def __call__(self, dev: Device, events: Sequence[Event]):
        cmds, mode = process_events(events, self.prev_mode)
        if mode:
            self.prev_mode = mode
        if not cmds:
            return
        logger.warning(
            f"Running RGB commands:\n{'\n'.join([cmd[:20].hex() for cmd in cmds])}"
        )
        for r in cmds:
            dev.write(r)


def switch_mode(dev: Device, mode: GamepadMode):
    match mode:
        case "default":
            cmds = COMMANDS_GAME
        # case "macro":
        #     cmds = MODE_MACRO
        case "mouse":
            cmds = COMMANDS_MOUSE
        case _:
            assert False, f"Mode '{mode}' not supported."

    for cmd in cmds:
        dev.write(cmd)
