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
from key_maps import *


class State:
  def __init__(self):
    key_map = NULL_KEY_MAP
    name = "NULL"
    use_rainbow = False
    rotary_label = ""
    control_volume = False
    update_frequency = 0.01
    isConfig = False
    encoder_last = 0

    def loop(self, macropad, text):
      encoder_position = macropad.encoder
      if encoder_position > self.encoder_last:
        if self.control_volume:
          macropad.consumer_control.send(
            macropad.ConsumerControlCode.VOLUME_INCREMENT
          )
          self.encoder_last = encoder_position
      if encoder_position < encoder_last:
        if self.control_volume:
          macropad.consumer_control.send(
            macropad.ConsumerControlCode.VOLUME_DECREMENT
          )
          self.encoder_last = encoder_position

      # send keyboard events mapped to keypad
      key_event = macropad.keys.events.get()
      if key_event:
        if key_event.pressed:
          key_num = key_event.key_number
          keys_to_send = self.key_map.get(key_num)[0]
          if keys_to_send:
            # toggle zoom video
            if key_num == 9:
              video_state = not video_state

            # toggle zoom audio
            if key_num == 10:
              vol_state = not vol_state

            # toggle_led_and_sound(key_num)

            keys_to_press = self.key_map[key_num][0]
            # what a hacky little check.
            if keys_to_press[0] is not None:
              kbd.press(*keys_to_press)
            kbd.release_all()

      text.show()

class ConfigState(State):
  def __init__(self):
    key_map = NULL_KEY_MAP
    name = "NULL"
    use_rainbow = False
    rotary_label = ""
    update_frequency = 0.01
    isConfig = False
    encoder_last = 0
    labels = [] # assume the order matches the runner order
    activeState = 0

    def get_selected_state(self):
      return self.activeState

    def add_label(self, label):
      self.labels.append(label)

    def loop(self, macropad, text):
      encoder_position = macropad.encoder
      if encoder_position > self.encoder_last:
        if activeState + 1 >= len(self.labels):
          activeState = 0
        else:
          activeState += 1
        self.encoder_last = encoder_position
      if encoder_position < encoder_last:
        if activeState - 1 <= 0:
          activeState = len(self.labels)-1
        else:
          activeState -= 1

        self.encoder_last = encoder_position
      text[3] = self.labels[activeState]
      text.show()
