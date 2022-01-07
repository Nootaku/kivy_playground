import os
os.environ["KIVY_VIDEO"] = 'ffpyplayer'


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen


class MenuWindow(Screen):
    pass


class WizardWindow(Screen):
    video_path = StringProperty()
    base_path = 'resources/videos/wizard/'
    video_list = [
        '01_fakie_gazelle.webm',
        '02_front_gazelle.webm',
        '03_lion_in_out.webm',
        '04_lion_out_in.webm',
    ]

    button_width = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.updateSizes()

    def updateSizes(self):
        self.button_width = int((self.width - dp(45)) / len(self.video_list))

    def launchVideo(self, video_index, player, menu):
        self.video_path = self.base_path + self.video_list[video_index]
        menu.height = 0
        menu.opacity = 0
        player.state = 'play'

    def stopVideo(self, player, menu):
        player.state = 'stop'
        menu.height = dp(45)
        menu.opacity = 1


class SlideWindow(Screen):
    video_path = StringProperty()
    video_list = [
        '01_fakie_gazelle.webm',
        '02_front_gazelle.webm',
        '03_lion_in_out.webm',
        '04_lion_out_in.webm',
    ]


class MainWindow(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create Menu
        self.createMenu()

    def createMenu(self):
        pass


class WheelWizardApp(App):
    pass


if __name__ == '__main__':
    app = WheelWizardApp()
    app.run()
