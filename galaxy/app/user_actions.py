def on_touch_down(self, touch):
    """Method called when the screen is being touched (smartphone / tablet)
    or when it is being cliked.
    """
    if touch.x < int(self.width / 2):
        self.current_movement_x = self.movement_speed_x
    else:
        self.current_movement_x = -self.movement_speed_x


def on_touch_up(self, touch):
    """Method called when the screen touch is being released.
    """
    self.current_movement_x = 0


def closeKeyboard(self):
    self._keyboard.unbind(on_key_down=self.onKeyDown)
    self._keyboard.unbind(on_key_up=self.onKeyRelease)
    self._keyboard = None


def onKeyDown(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.current_movement_x = self.movement_speed_x
    elif keycode[1] == 'right':
        self.current_movement_x = -self.movement_speed_x

    return True  # instruction that validates the keypress management


def onKeyRelease(self, keyboard, keycode):
    self.current_movement_x = 0
    return True
