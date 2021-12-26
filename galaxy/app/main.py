from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.properties import Clock, NumericProperty
from kivy.uix.widget import Widget


Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')


class MainWidget(Widget):
    # Initialization of the Perspective Points
    x_pp = NumericProperty(0)
    y_pp = NumericProperty(0)

    # Vertical Lines variables
    NB_V_LINES = 8
    V_LINES_SPACING = .2  # percentage of the window width
    vertical_lines = []

    # Horizontal Lines variables
    NB_H_LINES = 13
    H_LINES_SPACING = .1  # percentage of the window height
    horizontal_lines = []

    # Movement variables
    fps = 1 / 60
    movement_speed_y = 2.5
    movement_speed_x = 10
    current_offset_y = 0
    current_offset_x = 0
    current_movement_x = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create grid
        self.makeVerticalLines()
        self.makeHorizontalLines()

        # Movement
        Clock.schedule_interval(self.update, self.fps)

    def makeVerticalLines(self):
        """Generate vertical lines on the main interface.
        """
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_V_LINES):
                self.vertical_lines.append(
                    Line(width=1.5)
                )

    def makeHorizontalLines(self):
        """Generate horizontal lines on the main interface.
        """
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_H_LINES):
                self.horizontal_lines.append(
                    Line(width=1.5)
                )

    def updateVerticalLines(self, transform=True):
        """Update the position of the vertical lines depending on the size of
        the main inteface.
        Each line is separated by the defined line spacing. Since there are as
        many lines on the left as on the right, we can set the original offset
        to the negative value of half of the NB_V_LINES multiplied by the
        spacing.
        """
        offset = -int(self.NB_V_LINES / 2) + 0.5
        v_spacing = self.width * self.V_LINES_SPACING
        central_line_x = int(self.width / 2)

        for i in self.vertical_lines:
            line_x = int(
                central_line_x + (offset * v_spacing) + self.current_offset_x
            )
            x1, y1 = self.transformPerspective(
                line_x, 0) if transform else (int(line_x), 0)
            x2, y2 = self.transformPerspective(
                line_x, self.height) if transform else (
                    int(line_x), int(self.height)
                )
            i.points = [x1, y1, x2, y2]
            offset += 1

    def updateHorizontalLines(self, transform=True):
        """Horizontal lines should start at the left x-value of the vertical
        lines and stop at the right x- value of the vertical lines.
        To calculate this we re-use the code for vertical lines.
        Vertical spacing is calculated in the same manner as the vertical lines
        but with an offset of 0.
        """
        # Get x_min and x_max
        central_line_x = int(
            (self.width / 2) + self.current_offset_x
        )
        v_spacing = self.width * self.V_LINES_SPACING
        x_offset = int(self.NB_V_LINES / 2) - 0.5
        x_min = central_line_x + (x_offset * v_spacing)
        x_max = central_line_x - (x_offset * v_spacing)

        # Get y value
        h_spacing = self.height * self.H_LINES_SPACING

        for index, value in enumerate(self.horizontal_lines):
            line_y = (index * h_spacing) - self.current_offset_y
            x1, y1 = self.transformPerspective(x_min, line_y, transform)
            x2, y2 = self.transformPerspective(x_max, line_y, transform)
            value.points = [x1, y1, x2, y2]

    def transformPerspective(self, x, y, transform=True):
        """Create a mathematical computation of linear proportions for the
        drawn lines.

        Y-axis:
        This is a simple proportion: 100% = y_pp
        So n% = y_pp * n%

        X-axis:
        If y = 0 then X = 100% and if y = 100%, then x = 100% - x_diff
        where x_diff is the difference between the current x and the x_pp
        We can calculate this by applying the factor of the Y-axis to diff_x.
        """
        # linear vertical tranformation (y_max == y_pp)
        linear_y = (y / self.height) * self.y_pp
        if linear_y > self.y_pp:
            linear_y = self.y_pp

        # get the diff between the central point an the x at y = 0
        diff_x = x - self.x_pp

        # get the diff between the y_pp and linear_y
        # this corresponds to the difference between max y and y at x
        diff_y = self.y_pp - linear_y

        # get the y-factor² (= 1 when diff_y == y_pp AND = 0 when diff_y == 0)
        y_factor = (diff_y / self.y_pp) ** 4

        # final transformation
        transformation_x = self.x_pp + (diff_x * y_factor)
        transformation_y = self.y_pp * (1 - y_factor)

        if transform:
            return int(transformation_x), int(transformation_y)
        else:
            return int(x), int(y)

    def on_touch_down(self, touch):
        if touch.x < int(self.width / 2):
            self.current_movement_x = self.movement_speed_x
        else:
            self.current_movement_x = -self.movement_speed_x

    def on_touch_up(self, touch):
        self.current_movement_x = 0

    def update(self, dt):
        """Create the illusion of movement by updating 60 times per second.
        This means the 'on_size()' is no longer necessary as it will automatic-
        ally update.
        """
        # Time factor: normally == to 1 if real 60 fps
        time_factor = dt * 60
        self.updateVerticalLines()
        self.updateHorizontalLines()
        self.current_offset_y += self.movement_speed_y * time_factor
        self.current_offset_x += self.current_movement_x * time_factor

        # Reset to original position if zcond horizontal line reaches the
        # bottom of the screen.
        h_spacing = self.height * self.H_LINES_SPACING
        if self.current_offset_y >= h_spacing:
            self.current_offset_y -= h_spacing

# class VerticalLines():
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         with self.canvas:
#             Color(1, 1, 1)
#             for i in range(0, self.NB_V_LINES):
#                 self.vertical_lines.append(Line())


class GalaxyApp(App):
    pass


if __name__ == '__main__':
    galaxy = GalaxyApp()
    galaxy.run()
