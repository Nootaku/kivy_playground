# Kivy Minimal Application

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
