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

right = Keycode.RIGHT_ARROW
left = Keycode.LEFT_ARROW
ctrl = Keycode.LEFT_CONTROL
cmd = Keycode.COMMAND
shift = Keycode.LEFT_SHIFT
opt = Keycode.OPTION
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (204, 245, 2)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

NULL_KEY_MAP = {
    0: ([None], BLACK),
    1: ([None], BLACK),
    2: ([None], BLACK),
    3: ([None], BLACK),
    4: ([None], BLACK),
    5: ([None], BLACK),
    6: ([None], BLACK),
    7: ([None], BLACK),
    8: ([None], BLACK),
    9: ([None], BLACK),
    10: ([None], BLACK),   
    11: ([None], BLACK)
}

# maps the numeric macropad key number to a tuple containing an list of key(s) to send
# and the color to set the key to on the macropad
TEN_KEY_MAP = {
    0: ([Keycode.SEVEN], RED),
    1: ([Keycode.EIGHT], RED),
    2: ([Keycode.NINE], RED),
    3: ([Keycode.FOUR], RED),
    4: ([Keycode.FIVE], RED),
    5: ([Keycode.SIX], RED),
    6: ([Keycode.ONE], RED),
    7: ([Keycode.TWO], RED),
    8: ([Keycode.THREE], RED),
    9: ([Keycode.ZERO], RED),
    10: ([Keycode.BACKSPACE], RED),   
    11: ([Keycode.ENTER], RED)
}

TEST_KEY_MAP = {
    0: ([Keycode.ONE], WHITE),
    1: ([Keycode.TWO], WHITE),
    2: ([Keycode.THREE], WHITE),
    3: ([Keycode.FOUR], WHITE),
    4: ([Keycode.FIVE], WHITE),
    5: ([Keycode.SIX], WHITE),
    6: ([Keycode.SEVEN], WHITE),
    7: ([Keycode.EIGHT], WHITE),
    8: ([Keycode.NINE], WHITE),
    # toggle zoom audio
    9: ([cmd, shift, Keycode.A], RED),

    # toggle zoom video
    10: ([cmd, shift, Keycode.V], RED), 
    
    # toggle zoom floating meeting controls
    11: ([ctrl, opt, cmd, Keycode.H], YELLOW)
}