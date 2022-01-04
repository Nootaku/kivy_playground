"""Main code for the Galaxy project

Last update: 27-12-2021

Note:
In order for the defined window width and height to be registered, the
kivy.config and its methods need to be executed before any other imports.

This goes against PIP E402. So we will use another way.
"""

from kivy.uix.widget import Widget
from kivy.properties import Clock, NumericProperty
from kivy.core.window import Window
from kivy.config import Config
from kivy.app import App
from kivy import platform

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')


class MainWidget(Widget):
    """Main Widget of the application.
    Create a layout in perspective and validate user interaction.
    """
    # Internal imports
    from layout import (
        makeVerticalLines,
        makeHorizontalLines,
        getLineXFromIndex,
        getLineYFromIndex,
        updateVerticalLines,
        updateHorizontalLines
    )
    from tiles import (
        makeTiles,
        createFirstTenTiles,
        createTileCoordinates,
        getTileCoordinates,
        updateTiles
    )
    from ship import (
        makeShip,
        updateShip,
        updateShipGif
    )
    from transform import transformPerspective
    from user_actions import (
        on_touch_down,
        on_touch_up,
        onKeyDown,
        onKeyRelease,
        closeKeyboard
    )

    # Initialization of the Perspective Points
    x_pp = NumericProperty(0)
    y_pp = NumericProperty(0)
    use_perspective = True

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
    movement_speed_y = 1
    movement_speed_x = 5
    current_offset_y = 0
    current_offset_x = 0
    current_movement_x = 0
    current_loop_y = 0

    # Tile management
    NB_TILES = 15
    tiles = []
    tiles_coordinates = []
    tile_index_x = 0
    tile_index_y = 4

    # Spaceship management
    SHIP_WIDTH = 0.1
    SHIP_HEIGHT = 0.035
    SHIP_BASE = 0.04
    ship = None
    ship_coordinates = [(0, 0), (0, 0), (0, 0)]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set window size
        Window.size = (1200, 650)

        # Create grid
        self.makeVerticalLines()
        self.makeHorizontalLines()

        # Create tiles
        self.makeTiles()
        self.createFirstTenTiles()
        self.createTileCoordinates()

        # Create ship
        self.makeShip()

        # Keyboard input
        if self.isDesktop:
            self._keyboard = Window.request_keyboard(self.closeKeyboard, self)
            self._keyboard.bind(on_key_down=self.onKeyDown)
            self._keyboard.bind(on_key_up=self.onKeyRelease)

        # Movement
        Clock.schedule_interval(self.update, self.fps)

    @property
    def isDesktop(self):
        if platform in ['linux', 'win', 'macosx']:
            return True
        return False

    @property
    def centerX(self):
        return int(self.width / 2)

    def update(self, dt):
        """Create the illusion of movement by updating 60 times per second.
        This means the 'on_size()' is no longer necessary as it will automatic-
        ally update.
        """
        # Time factor: normally == to 1 if real 60 fps
        time_factor = dt * 60

        # Relative movement speed
        y_speed_unit = (self.height * self.H_LINES_SPACING) / 60
        y_movement_speed = y_speed_unit * self.movement_speed_y
        self.updateVerticalLines(self.use_perspective)
        self.updateHorizontalLines(self.use_perspective)
        self.updateTiles(self.use_perspective)
        self.updateShip(self.use_perspective)
        # self.updateShipGif()
        self.current_offset_y += y_movement_speed * time_factor
        self.current_offset_x += self.current_movement_x * time_factor

        # Reset to original position if zcond horizontal line reaches the
        # bottom of the screen.
        h_spacing = self.height * self.H_LINES_SPACING
        if self.current_offset_y >= h_spacing:
            self.current_offset_y -= h_spacing
            self.current_loop_y += 1
            # update the tile coordinates based on the current_loop_y
            self.createTileCoordinates()


class GalaxyApp(App):
    pass


if __name__ == '__main__':
    galaxy = GalaxyApp()
    galaxy.run()
