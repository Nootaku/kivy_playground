# Widgets

First we will have a brief introduction on how to use widgets. We will see how we can:

1. create a basic interaction between widgets and the application
2. create an interaction between two widgets
3.

Then we will have a look at different types of widgets and how we can use them.

## Introduction

In the _Layouts_ we have been using a lot of Buttons. However, none of these buttons did anything. Lets see a simple interaction between a Button and the application.

### Button => print to terminal

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

## Counters

foo

## IDs

bar

## Inputs

blah

## Images

meh
