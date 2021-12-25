from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class MainWindow(BoxLayout):
    pass


class VideoSelection(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(0, 10):
            element_size = dp(150)
            self.add_widget(
                Button(
                    text=f"Button_{str(i + 1)}",
                    size_hint=(.20, None),
                    height=element_size
                    # size=(element_size, element_size)
                )
            )


class WheelWizardApp(App):
    pass


if __name__ == '__main__':
    app = WheelWizardApp()
    app.run()
