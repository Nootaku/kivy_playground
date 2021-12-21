from kivy.app import App

# Layouts
from kivy.uix.gridlayout import GridLayout

# Properties
from kivy.properties import StringProperty


class WidgetsExample(GridLayout):
    text = StringProperty("Hello")

    def onButtonClick(self):
        print('Button Clicked')
        if self.text == "Hello":
            self.text = "World"
        else:
            self.text = "Hello"


class WidgetsTutorial(App):
    pass


if __name__ == '__main__':
    app = WidgetsTutorial()
    app.run()
