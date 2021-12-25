from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    # Initialization of the Perspective Points
    x_pp = NumericProperty(0)
    y_pp = NumericProperty(0)

    # Vertical Lines variables
    NB_V_LINES = 7  # should always be an odd number
    V_LINES_SPACING = .1  # percentage of the window width
    vertical_lines = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.verticalLines()

    def verticalLines(self):
        """Generate vertical lines on the main interface.
        """
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_V_LINES):
                self.vertical_lines.append(
                    Line(width=1.5)
                )

    def updateVerticalLines(self):
        """Update the position of the vertical lines depending on the size of
        the main inteface.
        Each line is separated by the defined line spacing. Since there are as
        many lines on the left as on the right, we can set the original offset
        to the negative value of half of the NB_V_LINES multiplied by the
        spacing.
        """
        offset = -int(self.NB_V_LINES / 2)
        spacing = self.width * self.V_LINES_SPACING
        central_line_x = int(self.width / 2)

        for i in self.vertical_lines:
            line_x = int(central_line_x + (offset * spacing))
            x1, y1 = self.transformPerspective(line_x, 0)
            x2, y2 = self.transformPerspective(line_x, self.height)
            i.points = [x1, y1, x2, y2]
            offset += 1

    def transformPerspective(self, x, y):
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
        # vertical tranformation (go to the height of y_pp)
        tranformation_y = (y / self.height) * self.y_pp
        if tranformation_y > self.y_pp:
            tranformation_y = self.y_pp

        # get the diff between the central point an the x at y = 0
        diff_x = x - self.x_pp

        # get the diff between the y_pp and transformation_y
        # this corresponds to the difference between max y and y at x
        diff_y = self.y_pp - tranformation_y

        # get the y-factor (= 1 when diff_y == y_pp AND = 0 when diff_y == 0)
        y_factor = diff_y / self.y_pp

        # horizontal transformation
        transformation_x = self.x_pp + (diff_x * y_factor)

        return int(transformation_x), int(tranformation_y)

    def on_size(self, *args):
        self.updateVerticalLines()


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
