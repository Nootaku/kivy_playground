from kivy.app import App

# Layouts
from kivy.uix.gridlayout import GridLayout

# Properties
from kivy.properties import StringProperty


class WidgetsExample(GridLayout):
    click_counter = 0
    text = StringProperty(str(click_counter))

    def onButtonClick(self):
        self.click_counter += 1
        self.text = str(self.click_counter)


class Exercice1(App):
    pass


if __name__ == '__main__':
    app = Exercice1()
    app.run()
