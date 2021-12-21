from kivy.app import App

# Layouts
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout

# Elements
from kivy.uix.button import Button

# Metrics
from kivy.metrics import dp


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(0, 150):
            element_size = dp(150)
            self.add_widget(
                Button(
                    text=f"Button_{str(i + 1)}",
                    size_hint=(None, None),
                    size=(element_size, element_size)
                )
            )


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class LayoutsTutorial(App):
    pass


if __name__ == '__main__':
    app = LayoutsTutorial()
    app.run()
