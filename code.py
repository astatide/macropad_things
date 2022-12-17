# SPDX-FileCopyrightText: 2022 Tali Herzka
#
# SPDX-License-Identifier: MIT

"""Keypad and rotary encoder example for Adafruit MacroPad"""

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_macropad import MacroPad
from rpc import RpcClient, RpcError
import usb_hid
import time
import asyncio
from rainbowio import colorwheel
# from adafruit_hid.consumer_control_code import ConsumerControlCode
from states import State, ConfigState
from runner import Runner
from key_maps import *

runner = Runner()
config = ConfigState()
ten_key = State()
ten_key.key_map = TEN_KEY_MAP
ten_key.use_rainbow = True
ten_key.name = "10-Key"
ten_key.control_volume = True
ten_key.rotary_enabled = True
ten_key.rotary_label = "Volume"
color_test = State()
color_test.name = "COLORTEST"
color_test.use_rainbow = True
off = State()
off.name = "OFF"
runner.AddState(config)
runner.AddState(ten_key, 0)
runner.AddState(color_test, 1)
runner.AddState(off, 2)
asyncio.run(runner.main())