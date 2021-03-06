# Galaxy

The galaxy project is a 2D game where the player aims at steering a spaceship on a track. If the player cannot follow the track, the game stops and it's a game over.

There are 3 steps to this project:

1. Create a grid, get it into perspective and generate movements.
2. Generate the track that the player has to follow, display the ship and handle collisions.
3. Finalization of the project by adding the menu, sounds and score.

## Step 1 - project creation

### Perspective point

The perspective point (**_pp_**) is the point where all the lines of perspective join. This point will be at 75% of the height of the window and 50% of its width. This should be independent of the size of the window (also on resize).

### Display vertical lines

Before using the perspective point, we will simply display the vertical lines. Applying the perspective will take place later.

Let's conceptualize what we want to do:<br/>
We want to create a number of vertical lines that are equally spaced and that are centered around the center of the window's width. The behavior should be consistent on resizing the window. This means that we need to create a line, then position it.

To do so, we first have to calculate the center of the width of the window: `int(self.width / 2)`.<br/>
Then we need to define a spacing (`V_LINES_SPACING = .1`). This spacing is a percentage of the full window width. The following concept is simply to put as many lines to the left of the central line as to the right of the central line. We can achieve this by creating a loop that starts at the negative value of `int(NB_V_LINES / 2)` and by incrementing this offset for each line in the loop.

Finally, we need to update the calculated position of the vertical lines when the window is being resized. So:<br/>

```python
def on_size(self, *args):
  self.updateVerticalLines()
```

### Perspective transformation

Now that we have our vertical lines, the transformation simply consists of changing the top point of the vertical lines. The top point should always be our perspective point.

The simplest way to do this is to apply the perspective point to the generated lines as top point. However, since we will have to calculate the horizontal lines as well, we want to create a transformation function that keeps us in control of each coordinate on the drawn lines.

[This video](https://www.youtube.com/watch?v=l8Imtec4ReQ&t=10511s) explains it pretty well.

### Display horizontal lines

We use the same strategy as for the vertical lines but for the horizontal lines. Then we improve the effect of perspective by decreasing the space between horizontal lines the closer they get to the perspective point.

## Step 2 - Movement

The impression of movement will be given by moving the vertical lines down. Once the Second vertical line reaches the bottom of the screen we will reset the lines to their original position and loop the animation.

To do this we can use the `Clock.schedule(f, dt)` function where `dt` is the time interval between 2 loops. The speed of the loop can be defined by the `y_offset` of the update function (the bigger, the faster).

## Step 3 - User input for horizontal movement

foo

## Step 4 - Tiles generation

In order to create tiles (or the road on which the spaceship will have to "drive"), we need to know "where" the tile should be generated. To do so we will use a **coordinate** system on a X - Y axes where Y = 0 at the very bottom of the screen and where X = 0 at the x coordinate of the perspective point.

This will make it possible to say: "create a tile at 3, 2"

In order to implement this system, we will consider that the bottom left corner of the tile is the coordinates.

And since we implemented our grid where the vertical lines are at `x - (0.5 * line_spacing)`, our coordinate `0, 0` will actually be at `-0.5, 0`.

### Displaying tiles

The first idea that popped in my mind when trying to generate a tile was to use a `Rectangle` and to transform it (like we did with the layout). However, the perspective transformation does not work on a `Rectangle`. This is why we will use a `Quad`.

The difference is that a `Quad` requires 4 points to be generated. And we can easily get those 4 points thanks to our `getLineXFromIndex()` and `getLineYFromIndex()` methods.

### Movement of the tiles

Since we use a looping mechanism to create the illusion of movement, tiles will "_jump_" back to their original position after each loop.

To prevent this we use a `loop_counter` and the Y coordinates of the tile will be the difference between the original Y and the current loop counter.

### Displaying multiple tiles

This part simply uses the generation of lists.

The first part is easy, we just use the same principle as for the line generation but we apply it to the tiles (loop through the number of tiles we want to generate).

The second part is a bit trickier: we want to be generating tiles infinitely.<br/>
To do this we need to adapt our `createTileCoordinates()` method.

### Generating turns

To make turns we are going to create 3 sample tiles (straight, left, right). All of those samples have one tile in common: `x, last_y_value + 1`.

Then we are going to take a random integer between 0 and 2 (included) where 0 is straight, 1 is left and 2 is right. Generating the sample shape described above. This forces us to also include a `last_x_value` variable.

#### Clean invisible tiles

The condition to be cleaned is that the `tile_index_y` is smaller than the `current_loop_y`.

## Step 5 - The ship

Creating the ship is simple: a `Triangle` that is being updated to screen height and width.

### Detection of collisions

The detection of collisions allows us to know if the ship "collides" with tiles. This detection uses the coordinates of the points of the ship and the `x_min`, `y_min`, `x_max`, `y_max` values of the tile.

If the x-coordinate of a point is between `x_min` and `x_max` and the y-coordinate between `y_min` and `y_max`, then it means the point is on the tile.<br/>
This corresponds to a collision.

Finally, we don't need to verify the collision with every tile but only with the 2 lowest rows as the ship does not move.

### Game Over

Now the collision allows us to know if the ship is on a tile. And tiles are the _path_ that the ship should follow. Which means that while the ship is colliding with tiles everything is ok, but as soon as the collision is `False`, the game should stop.

This is why we add a `is_game_over` parameter that is `False` by default and becomes `True` when no collision is detected.

Now that we have a state, we can modify our `update()` method to freeze when the state `is_game_over`.

## Step 6 - Adding the Menu

The menu is being handled by a different `.py` and `.kv` file.

Once the menu is created (as an independent widget), it can be included inside the `MainWidget` in the `galaxy.kv` file. To do so, we need to import it with `#:import menu menu`

```
#:import menu menu

MainWidget:

<MainWidget>:
    x_pp: self.width / 2
    y_pp: self.height * 0.8
    MenuWidget:
```

This on its own will not change anything. The menu will not appear.

To be able to display the menu, we need to use the kivy `Builder` in our `main.py`.

### Preventing game start: the 'Start' button

We are using the same method as the game over. We will create a `is_game_started` parameter that is false by default in our `main.py`. Only when `is_game_started == True` will the looping begin.

The parameter can be controlled by the `start` button in the menu. However, the `on_press` will not access the `root` (as it refers to the `<MenuWidget>`) but to the `root.parent` which corresponds to the Main widget.

But this is not enough.

The `on_touch_down()` method overwrites the clicking of a button. To ensure the good functioning of the button we need to make sure that the `on_touch_down()` method returns `super(MainWidget, self).on_touch_down(touch)`.

This is a very specific case. But we are not done yet:<br/>
`MainWidget` imports `user_actions.py` but in this case `user_actions.py` will need to import `MainWidget` creating a circular import.

To solve this, we will not import `MainWidget`, but its parent: `RelativeLayout`.

Finally, we need to know that if the opacity of the menu is 0, it does not mean that the menu is inactive. Which is why we need to disable the button when the `opacity == 0`.

### Restarting the game

Restarting the game is a little trickier than just saying that `is_game_over == False` and `is_game_started == True`.

The game uses multiple parameters (like `current_loop_y`, `current_offset_x`, etc) to determine the position. Moreover, the tiles have already been generated for the _n_ next iterations to come.

This is why we need to reset everything to zero and to empty the tiles and 're-generate' our first ten straight tiles.

# Kivy internal methods

## on_parent()

The `on_parent(self, widget, parent)` method is called when the widget is being attached to the parent element.

## on_size()

The `on_size(self, *args)` method is called whenever the window is being resized. This includes the resize that takes place right after the initialization of the main interface.

## on_touch_down()

When the screen is being touched (or if the mouse clicks on the window), the `on_touch_down(self, touch)` is being called. The position of the touch can be determined by using `touch.x` and `touch.y`.

## on_touch_up()

When the screen press is being released, the `on_touch_up(self, touch)` is being called.
