import random
from kivy.graphics import Color
from kivy.graphics import Quad


def makeTiles(self):
    """Generate tiles.
    """
    with self.canvas:
        Color(1, 1, 1)
        for i in range(self.NB_TILES):
            self.tiles.append(Quad())


def createFirstTenTiles(self):
    """Identical function to createTileCoordinates, but called only once at
    the start of the game.
    """
    for i in range(10):
        self.tiles_coordinates.append(
            (0, i)
        )


def createTileCoordinates(self):
    """For each generated tile, create the initial coordinate values of the
    tile.
    The function will be called at initialization of the layout as well as at
    each update loop.
    The path will then become inifinte and randomized by creating 3 basic
    shapes and appending them at random to the existing path.
    """
    # Varibales
    last_x_value = 0
    last_y_value = 0
    min_x = 1 - int(self.NB_V_LINES / 2)
    max_x = min_x + self.NB_V_LINES - 1

    # Cleanup the (tile) coordinates that are out of bounds
    for i in range(
        len(self.tiles_coordinates) - 1,  # maximum tile coordinate value
        -1,                               # we went to get to 0
        -1                                # with steps of -1
    ):
        y_value = self.tiles_coordinates[i][1]

        # If the tile is out of the screen
        if y_value < self.current_loop_y:
            del self.tiles_coordinates[i]

    # Update the last_y_value
    if len(self.tiles_coordinates) > 0:  # if not empty
        last_coordinates = self.tiles_coordinates[-1]
        last_x_value = last_coordinates[0]
        last_y_value = last_coordinates[1] + 1

    # Generate the (tile) coordinates
    # We should not start from null every time, but we should keep existing
    for i in range(len(self.tiles_coordinates), self.NB_TILES):
        rand = random.randint(0, 2)

        if last_x_value <= min_x:
            rand = 2
        if last_x_value >= max_x - 1:
            rand = 1

        # Common to all 3 shapes
        self.tiles_coordinates.append(
            (last_x_value, last_y_value)
        )

        # Go to the left
        if rand == 1:
            last_x_value -= 1
            self.tiles_coordinates.append(
                (last_x_value, last_y_value)
            )
            last_y_value += 1
            self.tiles_coordinates.append(
                (last_x_value, last_y_value)
            )

        # Go to the right
        if rand == 2:
            last_x_value += 1
            self.tiles_coordinates.append(
                (last_x_value, last_y_value)
            )
            last_y_value += 1
            self.tiles_coordinates.append(
                (last_x_value, last_y_value)
            )

        last_y_value += 1


def getTileCoordinates(self, tile_index_x, tile_index_y):
    """Return the x and y coordinates of a tile as a list.
    """
    looped_tile_index_y = tile_index_y - self.current_loop_y
    x_value = self.getLineXFromIndex(tile_index_x)
    y_value = self.getLineYFromIndex(looped_tile_index_y)

    return x_value, y_value


def updateTiles(self, transform=True):
    """euh
    """
    for i in range(self.NB_TILES):
        tile = self.tiles[i]
        tile_index_x = self.tiles_coordinates[i][0]
        tile_index_y = self.tiles_coordinates[i][1]
        x_min, y_min = self.getTileCoordinates(tile_index_x, tile_index_y)
        x_max, y_max = self.getTileCoordinates(
            tile_index_x + 1, tile_index_y + 1)

        if transform:
            x1, y1 = self.transformPerspective(x_min, y_min)
            x2, y2 = self.transformPerspective(x_min, y_max)
            x3, y3 = self.transformPerspective(x_max, y_max)
            x4, y4 = self.transformPerspective(x_max, y_min)

            tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]
        else:
            tile.points = [
                x_min, y_min, x_min, y_max, x_max, y_max, x_max, y_min
            ]
