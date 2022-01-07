from kivy.app import App
from kivy.uix.widget import Widget


class VideoWindow(Widget):
    pass


class WheelWizardApp(App):
    def build(self):
        return VideoWindow()


if __name__ == '__main__':
    app = WheelWizardApp()
    app.run()
