from kivy.graphics import Color
from kivy.graphics import Triangle
from kivy.uix.image import Image


def makeShip(self):
    with self.canvas:
        Color(0.25, 0.4, 1)
        self.ship = Triangle()
        # self.ship = Image(source='img/ship.gif', anim_delay=0, anim_loop=100)


def updateShip(self, transform=True):
    """Updates the position of the ship based on the size of the window.
    Also updates the 'ship_coordinates' to be used for collision detection.
    """
    center_x = self.width / 2
    base_y = self.SHIP_BASE * self.height
    ship_half_width = (self.SHIP_WIDTH * self.width) / 2
    ship_height = self.SHIP_HEIGHT * self.height

    # Triangle bottom left
    ship_x1 = int(center_x - ship_half_width)
    ship_y1 = int(base_y)

    # Triangle top
    ship_x2 = int(center_x)
    ship_y2 = int(base_y + ship_height)

    # Triangle bottom right
    ship_x3 = int(center_x + ship_half_width)
    ship_y3 = int(base_y)

    # Get current ship coordinates
    self.ship_coordinates[0] = (ship_x1, ship_y1)
    self.ship_coordinates[1] = (ship_x2, ship_y2)
    self.ship_coordinates[2] = (ship_x3, ship_y3)

    if transform:
        x1, y1 = self.transformPerspective(*self.ship_coordinates[0])
        x2, y2 = self.transformPerspective(*self.ship_coordinates[1])
        x3, y3 = self.transformPerspective(*self.ship_coordinates[2])

        self.ship.points = [x1, y1, x2, y2, x3, y3]

    else:
        self.ship.points = [
            ship_x1, ship_y1, ship_x2, ship_y2, ship_x3, ship_y3
        ]


def checkCollision(self):
    """Return True if the ship is on the track and return False if the ship
    is of the track.
    """
    for i in self.tiles_coordinates:
        tile_index_x, tile_index_y = i

        # We don't check the tiles that are not on the 2 first rows
        if tile_index_y > self.current_loop_y + 1:
            return False
        if self.checkShipCollisionWithTile(tile_index_x, tile_index_y):
            return True
    return False


def checkShipCollisionWithTile(self, tile_index_x, tile_index_y):
    """Check that the ship collides with a given tile.
    A collision is if at least 2 points of the triangle are inside the tile.
    The ship should collide with the road (aka tiles) as this is the aim of the
    game.
    """
    x_min, y_min = self.getTileCoordinates(tile_index_x, tile_index_y)
    x_max, y_max = self.getTileCoordinates(tile_index_x + 1, tile_index_y + 1)

    for i in self.ship_coordinates:
        point_x, point_y = i

        if x_min <= point_x <= x_max and y_min <= point_y <= y_max:
            return True

    return False


def updateShipGif(self):
    center_x = self.width / 2
    base_y = self.SHIP_BASE * self.height
    ship_width = self.SHIP_WIDTH * self.width
    ship_half_width = ship_width / 2
    ship_height = self.SHIP_HEIGHT * self.height

    ship_x1 = int(center_x - ship_half_width)
    ship_y1 = int(base_y)
    self.ship.pos = ship_x1, ship_y1
    # self.ship.size = ship_width, ship_height
