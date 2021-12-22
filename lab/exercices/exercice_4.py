from kivy.app import App

# Layouts
from kivy.uix.widget import Widget

from kivy.graphics.vertex_instructions import Rectangle


class MoveObject(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            self.rectangle = Rectangle(
                pos=(50, 100),
                size=(50, 50)
            )

    def onMoveButtonPress(self):
        x, y = self.rectangle.pos
        width, height = self.rectangle.size
        x += 10
        if x + width > self.width:
            pass
        else:
            self.rectangle.pos = (x, y)


class Exercice4(App):
    pass


if __name__ == '__main__':
    app = Exercice4()
    app.run()
