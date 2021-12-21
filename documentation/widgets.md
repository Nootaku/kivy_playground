# Widgets

First we will have a brief introduction on how to use widgets. We will see how we can:

1. create a basic interaction between widgets and the application
2. create an interaction between two widgets
3.

Then we will have a look at different types of widgets and how we can use them.

## Counters

### Introduction

In the _Layouts_ we have been using a lot of Buttons. However, none of these buttons did anything. Lets see a simple interaction between a Button and the application.

### Button interaction

#### Print to terminal

We first will create a `GridLayout`. This layout will have a method called `onButtonClick` and this method will print to the terminal.

To call the function, we can go in the `.kv` file and write:

```
<WidgetsExample>:
    cols: 3
    Button:
        text: 'Click here'
        on_press: root.onButtonClick()
    Label:
        text: 'Hello'
```

Notice the following:

- First, the `Button` has a `on_press` property. This property takes our `onButtonClick()` function as value.
- Second, the `onButtonClick()` function contains the parentheses. This is important as when calling a method it is pseudo-python code that is called.
- Third, the `root` preceding the method. This allows us to make the distinction between `self` and `root`.
  - `self` refers to the item that is currently being parameterized (in this case it would be the button)
  - `root` refers to the parent class (highest in the hierarchy). This means the `WidgetExample` class.

#### Exercice 1

Creation of a click-counter. The counter starts at 0 and increments with each click. The value of the counter is displayed as a label.

#### Exercice 2

Creation of a `ToggleButton` that enables or disables the previously made counter (enables if 'on' and disables if 'off').

### Using custom fonts

Simply add the `font_name` and `font_size` to your `Label`

### Disabled property

In the `.kv` file it is possible to add the `disabled` property on all widgets that can handle human interaction (like buttons, sliders etc.). This can be linked to a `BooleanProperty` in the python file.

It is important to note that to handle the opposite value of the `BooleanProperty` stored in the python file, we can use `disabled: not root.variable_name`.

## IDs

We can give an **ID** to widgets. This makes it possible to have multiple widgets communicate with each other. For example, if we want to have display the value of a slider, we could write a python function that handles this behavior.<br/>
This function has been the objective of _Exercice 3_.

However by using the `id` parameter in the `.kv` file, it is easier and faster to obtain the exact same behavior.

```
Slider:
    id: my_slider
Label:
    text: str(my_slider.value)
```

## Inputs

We want to be able to give the user the ability to input text in our application.

For this we use the `TextInput`. This can have multiple properties but the most important ones to remember are:

- muliline: BooleanProperty
- on_validate: when we press 'enter' on a single line input

## Images

Inserting images is pretty easy, simply call an `Image` widget giving it the desired `source`.

Here is an example with three identical sources:

```
<GridLayout>:
    cols: 3
    Image:
        source: "images/test_image.jpg"
    Image:
        source: "images/test_image.jpg"
        allow_stretch: True
    Image:
        source: "images/test_image.jpg"
        allow_stretch: True
        keep_ratio: False
```

- `allow_stretch` makes it possible for the image to become bigger than it's original size (impossible by default)
- `keep_ratio: False` will allow the image to break the ratio of the source and cover the entire surface of allocated to the widget. This parameter only takes effect if both `allow_stretch: True` and `keep_ratio: False`.
