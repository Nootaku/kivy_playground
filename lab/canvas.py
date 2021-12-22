from kivy.app import App
from kivy.graphics.vertex_instructions import Ellipse
from kivy.metrics import dp
from kivy.properties import BooleanProperty, Clock, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    click_counter = 0
    is_counter_active = BooleanProperty(False)
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


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CenteredCross(Widget):
    pass


class MoveObject(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ball_size = dp(50)
        self.x_velocity = dp(3)
        self.y_velocity = dp(4)

        with self.canvas:
            self.ball = Ellipse(
                pos=(50, 50),
                size=(self.ball_size, self.ball_size)
            )

        Clock.schedule_interval(self.updateBallPosition, 1/60)

    def on_size(self, *args):
        self.ball.pos = (
            self.center_x - self.ball_size / 2,
            self.center_y - self.ball_size / 2
        )

    def updateBallPosition(self, dt):
        # Get initial values
        x, y = self.ball.pos

        # Update values
        x += self.x_velocity
        y += self.y_velocity

        # Check if values are in frame
        is_right = self.ball_size + x > self.width
        is_top = self.ball_size + y > self.height
        is_left = x < 0
        is_bottom = y < 0

        if is_left:
            x = 0
            self.x_velocity = -self.x_velocity

        if is_right:
            x = self.width - self.ball_size
            self.x_velocity = -self.x_velocity

        if is_bottom:
            y = 0
            self.y_velocity = -self.y_velocity

        if is_top:
            y = self.height - self.ball_size
            self.y_velocity = -self.y_velocity

        self.ball.pos = (x, y)


class CanvasTutorial(App):
    pass


if __name__ == '__main__':
    app = CanvasTutorial()
    app.run()
