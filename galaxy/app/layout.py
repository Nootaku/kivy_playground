from kivy.graphics import Line
from kivy.graphics import Color


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
