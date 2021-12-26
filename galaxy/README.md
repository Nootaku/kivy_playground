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

## Kivy internal methods

### on_parent()

The `on_parent(self, widget, parent)` method is called when the widget is being attached to the parent element.

### on_size()

The `on_size(self, *args)` method is called whenever the window is being resized. This includes the resize that takes place right after the initialization of the main interface.