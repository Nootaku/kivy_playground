# Kivy

These file contains notes on how a Kivy application works. We will go through a minimal application and its different layouts and canvases.

## Minimal application

To work a Kivy project needs at least a **_`main.py`_** file and a **_`<appName>.kv`_** file.

### main.py

The `main.py` file should at least contain two classes and the code to run the app. We can see the code below:

```python
from kivy.app import App
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


if __name__ == '__main__':
    app = TheLabApp()
    app.run()
```

Here are some important elements to highlight:

- The `App` class' name should always end with `App` (here we name it `TheLabApp`)
- Only an instance of the `App` class can be run. So you can either use a variable like we did, or run it as `TheLabApp().run()`.

### The .kv file

The `<appName>.kv` file should be named with the **exact same name** as the class that we are _running_ in `main.py` but in **_full lowercase_**. In this case it will be called `thelab.kv`<br/>
The `.kv` file will contain the _definition of our graphical interface_. Also, even though it is **possible** to generate the graphical interface directly from `main.py` it is recommended (for both documentation and readability) to use the `.kv` file.

#### Structure

At the top of your file, start by type the name of your main instance followed by a semi-colon (`:`). In our case this will be the `MainWidget` class.

Afterwards it works in a way similar to a `yaml` or `toml` file. It uses a key-value syntax were objects are indicated by an indentation and each key of the object is on its own line.

##### Information

When an item is added to the window;

- the default position will always be at pixel `0, 0` (x-axis, y-axis). In human words, this means on the bottom left.
  - is controlled by the `pos` key
  - if two elements are on the same position, only the last element will be visible. (stacked layout)
- the default size will always be 100 x 100 px.
  - is controlled by the `size` key
- the default unit of placement and size is pixels. But pixels have different sizes on different displays. To alleviate this problem, we can use density-independent pixels. This is done by using the syntax `"400dp", "200dp"`.
  - `dp` corresponds to a physical size. Consider that `"40dp", "40dp"` is the size of a finger touch. (= ideal for a small button)

## Layouts

### Box Layout

A `BoxLayout` is a layout that is considered as a _box_. This means that all the content of the box will have the default behavior of the elements of a widget. But a box can contain other boxes and / or widgets making it possible to layer multiple layouts.

### Anchor Layout

The `AnchorLayout` will always use 100% of its allocated space and it is impossible to 'stack' is elements as the allocated space will be identical for both elements. This means that if an Anchor Layout is the primary layout, we can only create multiple elements by creating another layout as child that will itself contain the stacked elements.

### Grid Layout

The `GridLayout` allows the organization of elements in _Rows_ and _Columns_. The difference between the box layout and the grid layout is that the grid layout will automatically create a new row or column when it's defined count of element has been reached.

### Stack Layout

The `StackLayout` is very similar to the grid layout but instead of giving it a number of elements, we give the elements a size. When the sum of the sizes of the elements reach 100% of the window width (or height if setup that way), a new row (or column) will automatically be generated for the following elements.

This layout is very efficient to programmatically generate a list of elements. This takes place in the `main.py` file and not in the `.kv` file.

```python
class StackLayoutExample(StackLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

    for i in range(0, 150):
      element_size = dp(60)
      self.add_widget(
        Button(
          text=f"Button_{str(i)}",
          size_hint=(None, None),
          size=(element_size, element_size)
        )
      )
```

### Scroll View

The `ScrollView` is not really a layout, it is a way to display a layout. A scroll view can only have one child: another layout.<br/>
The possible arguments for the scroll view are the size of the child. Adapting the `size_hint` of the child can define whether the scroll should be horizontal or vertical (in the example below it is vertical) and the `size` (or `height` / `width`) parameters define how much can be scrolled. The special variables `self.minimum_height` and `self.minimum_width` represent the real-time dynamic values of the child elements.

```
ScrollViewExample:

<ScrollViewExample@ScrollView>:
    StackLayoutExample:
        size_hint: 1, None
        height: self.minimum_height
```

**Warning:** In order for this to work properly, the size of the children of the child element (in this case the `Buttons` of the `StackLayoutExample`) MUST be fixed. This means that the `size_hint` of the scroll direction should be `None`.

### Page Layout

The `PageLayout` makes it possible to go from one layout to the other. It take the layouts that we want to be able to switch to as arguments. The default behaviour is a scroll-left / right to go to the previous / next layout.

## Widgets

### Counters

foo

### IDs

bar

### Inputs

blah

### Images

meh
