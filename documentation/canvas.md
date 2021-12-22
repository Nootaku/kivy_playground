# Kivy Canvases

The canvases allow to draw lines and shapes on the screen. It also allows us to move those lines and shapes allowing our application to display **graphical instructions**.

The second objective is to understand the interaction between the Canvas an the Widgets.

The third objective is an exercice that aims at moving a ball with the Move instructions.

## Draw a shape

To draw a shape, simply use the `canvas` widget and create one of the shapes as child element (`Rectangle`, `Ellipse`, ...)

### Draw a Line

Drawing a line is similar to drawing a shape. It also takes place inside the `canvas` widget. But a line is drawn between two positions or points on the canvas.<br/>
`points: (x, y, x2, y2)`

### Draw an empty shape

Using shapes automatically fills the shape with color. However, we can also use the `Line` to create shapes. this is done as follows:

```
<Widget>:
    canvas:
        Line:
            circle: (200, 200, 100) # center_x, center_y, radius
            width: 2                # thickness of the line
```

## Create movement

Using the `canvas` programmatically, it is possible to update the `pos` values of a shape or object.

In Exercise 4 we create a button that moves a rectangle to the right of the screen.

## Ball animation

The objective of this chapter is to create a ball that starts in the center of the window and will move in a random direction until it hits a border and will then continue its movement in the opposite direction. Basically, just like the windows 98 screensaver ;-)<br/>
To do this we will use a function using a `time.sleep()`. This means the ball should be created programmatically.

The first thing we can learn from this exercise is that objects created in the `__init__` function of the interface cannot access the inner values of the interface (like width or height). These values are being defined after the initialization in the `on_size()` method.

##
