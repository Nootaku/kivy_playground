from kivy.app import App

# Layouts
from kivy.uix.gridlayout import GridLayout

# Properties
from kivy.properties import StringProperty


class WidgetsExample(GridLayout):
    click_counter = 0
    is_counter_active = False
    text = StringProperty(str(click_counter))

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


class Exercice2(App):
    pass


if __name__ == '__main__':
    app = Exercice2()
    app.run()
