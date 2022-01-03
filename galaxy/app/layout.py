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


def getLineXFromIndex(self, index):
    """Return the X value (value of the horizontal axis) of a vertical line on
    the grid based on the line index.
    """
    central_x = self.x_pp
    spacing = self.V_LINES_SPACING * self.width
    offset = index - 0.5

    line_x = central_x + (offset * spacing) + self.current_offset_x

    return line_x


def getLineYFromIndex(self, index):
    """Return the Y value (value of the vertical axis) of a horizontal line on
    the grid based on the line index.
    """
    spacing = self.H_LINES_SPACING * self.height
    y_value = index * spacing
    line_y = y_value - self.current_offset_y

    return line_y


def updateVerticalLines(self, transform=True):
    """Update the position of the vertical lines depending on the size of
    the main inteface.
    Each line is separated by the defined line spacing. Since there are as
    many lines on the left as on the right, we can set the original offset
    to the negative value of half of the NB_V_LINES multiplied by the
    spacing.
    """
    start_line = 1 - int(self.NB_V_LINES / 2)
    end_line = start_line + self.NB_V_LINES

    for i in range(start_line, end_line):
        line_x = self.getLineXFromIndex(i)
        x1, y1 = self.transformPerspective(
            line_x, 0) if transform else (int(line_x), 0)
        x2, y2 = self.transformPerspective(
            line_x, self.height) if transform else (
                int(line_x), int(self.height)
            )
        self.vertical_lines[i].points = [x1, y1, x2, y2]


def updateHorizontalLines(self, transform=True):
    """Horizontal lines should start at the left x-value of the vertical
    lines and stop at the right x- value of the vertical lines.
    To calculate this we re-use the code for vertical lines.
    Vertical spacing is calculated in the same manner as the vertical lines
    but with an offset of 0.
    """
    # Get x_min and x_max
    start_index = 1 - int(self.NB_V_LINES / 2)
    end_index = start_index + self.NB_V_LINES - 1

    x_min = self.getLineXFromIndex(start_index)
    x_max = self.getLineXFromIndex(end_index)

    for index, value in enumerate(self.horizontal_lines):
        line_y = self.getLineYFromIndex(index)
        x1, y1 = self.transformPerspective(x_min, line_y, transform)
        x2, y2 = self.transformPerspective(x_max, line_y, transform)
        value.points = [x1, y1, x2, y2]
