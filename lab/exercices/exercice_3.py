from kivy.app import App

# Layouts
from kivy.uix.gridlayout import GridLayout

# Properties
from kivy.properties import BooleanProperty, StringProperty


class WidgetsExample(GridLayout):
    click_counter = 0
    is_counter_active = BooleanProperty(False)
    text = StringProperty(str(click_counter))

    is_slider_active = BooleanProperty(False)
    slider_text = StringProperty("50")

    def onCount(self):
        if self.is_counter_active:
            self.click_counter += 1
            self.text = str(self.click_counter)

    def onToggle(self, widget):
        if widget.state == 'normal':
            # This is the OFF
            widget.text = 'Off'
            self.is_counter_active = False
        else:
            # This is the ON
            widget.text = 'On'
            self.is_counter_active = True

    def onSwitch(self, widget):
        if widget.active:
            self.is_slider_active = True
        else:
            self.is_slider_active = False

    def onSlider(self, widget):
        self.slider_text = str(int(widget.value))


class Exercice3(App):
    pass


if __name__ == '__main__':
    app = Exercice3()
    app.run()
