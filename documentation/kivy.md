# Kivy

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

The `<appName>.kv` file should be named with the **exact same name** as the class that we are _running_ in `main.py`. In this case it will be called `TheLab.kv`<br/>
The `.kv` file will contain the _definition of our graphical interface_. Also, even though it is **possible** to generate the graphical interface directly from `main.py` it is recommended (for both documentation and readability) to use the `.kv` file.

#### Structure

At the top of your file, start by type the name of your main instance followed by a semi-colon (`:`). In our case this will be the `MainWidget` class.
