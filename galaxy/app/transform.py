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
