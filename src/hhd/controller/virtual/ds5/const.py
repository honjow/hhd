from hhd.controller import Axis, Button
from hhd.controller.lib.common import AM, BM
from hhd.controller.lib.uhid import BUS_USB

DS5_EDGE_VENDOR = 0x054C
DS5_EDGE_PRODUCT = 0x0DF2
DS5_EDGE_VERSION = 0
DS5_EDGE_COUNTRY = 0
DS5_EDGE_BUS = BUS_USB
DS5_EDGE_NAME = b"Emulated Sony DS5 Edge Controller"

DS5_EDGE_MIN_REPORT_FREQ = 25
DS5_EDGE_MAX_REPORT_FREQ = 1000
DS5_EDGE_DELTA_TIME = 4096.0


def _prep_def_report():
    d = bytearray(64)
    d[0] = 0x01

    d[62] = 0x80
    d[57] = 0x80
    d[53] = 0x80
    d[48] = 0x80
    d[35] = 0x80
    d[44] = 0x80

    return bytes(d)


DS5_EDGE_REPORT_USB_BASE = _prep_def_report()

DS5_EDGE_DESCRIPTOR = bytes(
    [
        0x05,
        0x01,  # Usage Page (Generic Desktop)        0
        0x09,
        0x05,  # Usage (Game Pad)                    2
        0xA1,
        0x01,  # Collection (Application)            4
        0x85,
        0x01,  #  Report ID (1)                      6
        0x09,
        0x30,  #  Usage (X)                          8
        0x09,
        0x31,  #  Usage (Y)                          10
        0x09,
        0x32,  #  Usage (Z)                          12
        0x09,
        0x35,  #  Usage (Rz)                         14
        0x09,
        0x33,  #  Usage (Rx)                         16
        0x09,
        0x34,  #  Usage (Ry)                         18
        0x15,
        0x00,  #  Logical Minimum (0)                20
        0x26,
        0xFF,
        0x00,  #  Logical Maximum (255)              22
        0x75,
        0x08,  #  Report Size (8)                    25
        0x95,
        0x06,  #  Report Count (6)                   27
        0x81,
        0x02,  #  Input (Data,Var,Abs)               29
        0x06,
        0x00,
        0xFF,  #  Usage Page (Vendor Defined Page 1) 31
        0x09,
        0x20,  #  Usage (Vendor Usage 0x20)          34
        0x95,
        0x01,  #  Report Count (1)                   36
        0x81,
        0x02,  #  Input (Data,Var,Abs)               38
        0x05,
        0x01,  #  Usage Page (Generic Desktop)       40
        0x09,
        0x39,  #  Usage (Hat switch)                 42
        0x15,
        0x00,  #  Logical Minimum (0)                44
        0x25,
        0x07,  #  Logical Maximum (7)                46
        0x35,
        0x00,  #  Physical Minimum (0)               48
        0x46,
        0x3B,
        0x01,  #  Physical Maximum (315)             50
        0x65,
        0x14,  #  Unit (EnglishRotation: deg)        53
        0x75,
        0x04,  #  Report Size (4)                    55
        0x95,
        0x01,  #  Report Count (1)                   57
        0x81,
        0x42,  #  Input (Data,Var,Abs,Null)          59
        0x65,
        0x00,  #  Unit (None)                        61
        0x05,
        0x09,  #  Usage Page (Button)                63
        0x19,
        0x01,  #  Usage Minimum (1)                  65
        0x29,
        0x0F,  #  Usage Maximum (15)                 67
        0x15,
        0x00,  #  Logical Minimum (0)                69
        0x25,
        0x01,  #  Logical Maximum (1)                71
        0x75,
        0x01,  #  Report Size (1)                    73
        0x95,
        0x0F,  #  Report Count (15)                  75
        0x81,
        0x02,  #  Input (Data,Var,Abs)               77
        0x06,
        0x00,
        0xFF,  #  Usage Page (Vendor Defined Page 1) 79
        0x09,
        0x21,  #  Usage (Vendor Usage 0x21)          82
        0x95,
        0x0D,  #  Report Count (13)                  84
        0x81,
        0x02,  #  Input (Data,Var,Abs)               86
        0x06,
        0x00,
        0xFF,  #  Usage Page (Vendor Defined Page 1) 88
        0x09,
        0x22,  #  Usage (Vendor Usage 0x22)          91
        0x15,
        0x00,  #  Logical Minimum (0)                93
        0x26,
        0xFF,
        0x00,  #  Logical Maximum (255)              95
        0x75,
        0x08,  #  Report Size (8)                    98
        0x95,
        0x34,  #  Report Count (52)                  100
        0x81,
        0x02,  #  Input (Data,Var,Abs)               102
        0x85,
        0x02,  #  Report ID (2)                      104
        0x09,
        0x23,  #  Usage (Vendor Usage 0x23)          106
        0x95,
        0x3F,  #  Report Count (63)                  108
        0x91,
        0x02,  #  Output (Data,Var,Abs)              110
        0x85,
        0x05,  #  Report ID (5)                      112
        0x09,
        0x33,  #  Usage (Vendor Usage 0x33)          114
        0x95,
        0x28,  #  Report Count (40)                  116
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             118
        0x85,
        0x08,  #  Report ID (8)                      120
        0x09,
        0x34,  #  Usage (Vendor Usage 0x34)          122
        0x95,
        0x2F,  #  Report Count (47)                  124
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             126
        0x85,
        0x09,  #  Report ID (9)                      128
        0x09,
        0x24,  #  Usage (Vendor Usage 0x24)          130
        0x95,
        0x13,  #  Report Count (19)                  132
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             134
        0x85,
        0x0A,  #  Report ID (10)                     136
        0x09,
        0x25,  #  Usage (Vendor Usage 0x25)          138
        0x95,
        0x1A,  #  Report Count (26)                  140
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             142
        0x85,
        0x20,  #  Report ID (32)                     144
        0x09,
        0x26,  #  Usage (Vendor Usage 0x26)          146
        0x95,
        0x3F,  #  Report Count (63)                  148
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             150
        0x85,
        0x21,  #  Report ID (33)                     152
        0x09,
        0x27,  #  Usage (Vendor Usage 0x27)          154
        0x95,
        0x04,  #  Report Count (4)                   156
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             158
        0x85,
        0x22,  #  Report ID (34)                     160
        0x09,
        0x40,  #  Usage (Vendor Usage 0x40)          162
        0x95,
        0x3F,  #  Report Count (63)                  164
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             166
        0x85,
        0x80,  #  Report ID (128)                    168
        0x09,
        0x28,  #  Usage (Vendor Usage 0x28)          170
        0x95,
        0x3F,  #  Report Count (63)                  172
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             174
        0x85,
        0x81,  #  Report ID (129)                    176
        0x09,
        0x29,  #  Usage (Vendor Usage 0x29)          178
        0x95,
        0x3F,  #  Report Count (63)                  180
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             182
        0x85,
        0x82,  #  Report ID (130)                    184
        0x09,
        0x2A,  #  Usage (Vendor Usage 0x2a)          186
        0x95,
        0x09,  #  Report Count (9)                   188
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             190
        0x85,
        0x83,  #  Report ID (131)                    192
        0x09,
        0x2B,  #  Usage (Vendor Usage 0x2b)          194
        0x95,
        0x3F,  #  Report Count (63)                  196
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             198
        0x85,
        0x84,  #  Report ID (132)                    200
        0x09,
        0x2C,  #  Usage (Vendor Usage 0x2c)          202
        0x95,
        0x3F,  #  Report Count (63)                  204
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             206
        0x85,
        0x85,  #  Report ID (133)                    208
        0x09,
        0x2D,  #  Usage (Vendor Usage 0x2d)          210
        0x95,
        0x02,  #  Report Count (2)                   212
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             214
        0x85,
        0xA0,  #  Report ID (160)                    216
        0x09,
        0x2E,  #  Usage (Vendor Usage 0x2e)          218
        0x95,
        0x01,  #  Report Count (1)                   220
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             222
        0x85,
        0xE0,  #  Report ID (224)                    224
        0x09,
        0x2F,  #  Usage (Vendor Usage 0x2f)          226
        0x95,
        0x3F,  #  Report Count (63)                  228
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             230
        0x85,
        0xF0,  #  Report ID (240)                    232
        0x09,
        0x30,  #  Usage (Vendor Usage 0x30)          234
        0x95,
        0x3F,  #  Report Count (63)                  236
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             238
        0x85,
        0xF1,  #  Report ID (241)                    240
        0x09,
        0x31,  #  Usage (Vendor Usage 0x31)          242
        0x95,
        0x3F,  #  Report Count (63)                  244
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             246
        0x85,
        0xF2,  #  Report ID (242)                    248
        0x09,
        0x32,  #  Usage (Vendor Usage 0x32)          250
        0x95,
        0x34,  #  Report Count (52)                  252
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             254
        0x85,
        0xF4,  #  Report ID (244)                    256
        0x09,
        0x35,  #  Usage (Vendor Usage 0x35)          258
        0x95,
        0x3F,  #  Report Count (63)                  260
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             262
        0x85,
        0xF5,  #  Report ID (245)                    264
        0x09,
        0x36,  #  Usage (Vendor Usage 0x36)          266
        0x95,
        0x03,  #  Report Count (3)                   268
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             270
        0x85,
        0x60,  #  Report ID (96)                     272
        0x09,
        0x41,  #  Usage (Vendor Usage 0x41)          274
        0x95,
        0x3F,  #  Report Count (63)                  276
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             278
        0x85,
        0x61,  #  Report ID (97)                     280
        0x09,
        0x42,  #  Usage (Vendor Usage 0x42)          282
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             284
        0x85,
        0x62,  #  Report ID (98)                     286
        0x09,
        0x43,  #  Usage (Vendor Usage 0x43)          288
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             290
        0x85,
        0x63,  #  Report ID (99)                     292
        0x09,
        0x44,  #  Usage (Vendor Usage 0x44)          294
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             296
        0x85,
        0x64,  #  Report ID (100)                    298
        0x09,
        0x45,  #  Usage (Vendor Usage 0x45)          300
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             302
        0x85,
        0x65,  #  Report ID (101)                    304
        0x09,
        0x46,  #  Usage (Vendor Usage 0x46)          306
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             308
        0x85,
        0x68,  #  Report ID (104)                    310
        0x09,
        0x47,  #  Usage (Vendor Usage 0x47)          312
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             314
        0x85,
        0x70,  #  Report ID (112)                    316
        0x09,
        0x48,  #  Usage (Vendor Usage 0x48)          318
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             320
        0x85,
        0x71,  #  Report ID (113)                    322
        0x09,
        0x49,  #  Usage (Vendor Usage 0x49)          324
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             326
        0x85,
        0x72,  #  Report ID (114)                    328
        0x09,
        0x4A,  #  Usage (Vendor Usage 0x4a)          330
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             332
        0x85,
        0x73,  #  Report ID (115)                    334
        0x09,
        0x4B,  #  Usage (Vendor Usage 0x4b)          336
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             338
        0x85,
        0x74,  #  Report ID (116)                    340
        0x09,
        0x4C,  #  Usage (Vendor Usage 0x4c)          342
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             344
        0x85,
        0x75,  #  Report ID (117)                    346
        0x09,
        0x4D,  #  Usage (Vendor Usage 0x4d)          348
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             350
        0x85,
        0x76,  #  Report ID (118)                    352
        0x09,
        0x4E,  #  Usage (Vendor Usage 0x4e)          354
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             356
        0x85,
        0x77,  #  Report ID (119)                    358
        0x09,
        0x4F,  #  Usage (Vendor Usage 0x4f)          360
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             362
        0x85,
        0x78,  #  Report ID (120)                    364
        0x09,
        0x50,  #  Usage (Vendor Usage 0x50)          366
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             368
        0x85,
        0x79,  #  Report ID (121)                    370
        0x09,
        0x51,  #  Usage (Vendor Usage 0x51)          372
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             374
        0x85,
        0x7A,  #  Report ID (122)                    376
        0x09,
        0x52,  #  Usage (Vendor Usage 0x52)          378
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             380
        0x85,
        0x7B,  #  Report ID (123)                    382
        0x09,
        0x53,  #  Usage (Vendor Usage 0x53)          384
        0xB1,
        0x02,  #  Feature (Data,Var,Abs)             386
        0xC0,  # End Collection                      388
    ]
)

DS5_EDGE_MAC_ADDR = [0x74, 0xE7, 0xD6, 0x3A, 0x47, 0xE8]
DS5_EDGE_STOCK_REPORTS = {
    0x09: bytes(  # Pairing
        [
            0x09,
            DS5_EDGE_MAC_ADDR[0],
            DS5_EDGE_MAC_ADDR[1],
            DS5_EDGE_MAC_ADDR[2],
            DS5_EDGE_MAC_ADDR[3],
            DS5_EDGE_MAC_ADDR[4],
            DS5_EDGE_MAC_ADDR[5],
            0x08,
            0x25,
            0x00,
            0x1E,
            0x00,
            0xEE,
            0x74,
            0xD0,
            0xBC,
            0x00,
            0x00,
            0x00,
            0x00,
        ]
    ),
    0x20: bytes(  # Firmware Info
        [
            0x20,
            0x4A,
            0x75,
            0x6E,
            0x20,
            0x31,
            0x39,
            0x20,
            0x32,
            0x30,
            0x32,
            0x33,
            0x31,
            0x34,
            0x3A,
            0x34,
            0x37,
            0x3A,
            0x33,
            0x34,
            0x03,
            0x00,
            0x44,
            0x00,
            0x08,
            0x02,
            0x00,
            0x01,
            0x36,
            0x00,
            0x00,
            0x01,
            0xC1,
            0xC8,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x54,
            0x01,
            0x00,
            0x00,
            0x14,
            0x00,
            0x00,
            0x00,
            0x0B,
            0x00,
            0x01,
            0x00,
            0x06,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
        ]
    ),
    0x05: bytes(  # Calibration
        [
            0x05,
            0xFE,
            0xFF,
            0xFC,
            0xFF,
            0xFE,
            0xFF,
            0x83,
            0x22,
            0x78,
            0xDD,
            0x92,
            0x22,
            0x5F,
            0xDD,
            0x95,
            0x22,
            0x6D,
            0xDD,
            0x1C,
            0x02,
            0x1C,
            0x02,
            0xF2,
            0x1F,
            0xED,
            0xDF,
            0xE3,
            0x20,
            0xDA,
            0xE0,
            0xEE,
            0x1F,
            0xDF,
            0xDF,
            0x0B,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
        ]
    ),
}


DS5_AXIS_MAP: dict[Axis, AM] = {
    "gyro_x": AM((16 << 3), "i16", scale=5729.6),
    "gyro_y": AM((18 << 3), "i16", scale=5729.6),
    "gyro_z": AM((20 << 3), "i16", scale=5729.6),
    "accel_x": AM((22 << 3), "i16", scale=10.19716),
    "accel_y": AM((24 << 3), "i16", scale=10.19716),
    "accel_z": AM((26 << 3), "i16", scale=10.19716),
}
DS5_BUTTON_MAP: dict[Button, BM] = {}
