def on_touch_down(self, touch):
    """Method called when the screen is being touched (smartphone / tablet)
    or when it is being cliked.
    """
    x_speed_unit = (self.width * self.V_LINES_SPACING) / 60
    x_movement_speed = x_speed_unit * self.movement_speed_x

    if touch.x < int(self.width / 2):
        self.current_movement_x = x_movement_speed
    else:
        self.current_movement_x = -x_movement_speed


def on_touch_up(self, touch):
    """Method called when the screen touch is being released.
    """
    self.current_movement_x = 0


def closeKeyboard(self):
    self._keyboard.unbind(on_key_down=self.onKeyDown)
    self._keyboard.unbind(on_key_up=self.onKeyRelease)
    self._keyboard = None


def onKeyDown(self, keyboard, keycode, text, modifiers):
    """Method called when the keyboard is pressed.
    """
    x_speed_unit = (self.width * self.V_LINES_SPACING) / 60
    x_movement_speed = x_speed_unit * self.movement_speed_x

    if keycode[1] == 'left':
        self.current_movement_x = x_movement_speed
    elif keycode[1] == 'right':
        self.current_movement_x = -x_movement_speed

    return True  # instruction that validates the keypress management


def onKeyRelease(self, keyboard, keycode):
    self.current_movement_x = 0
    return True
