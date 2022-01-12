import os
os.environ["KIVY_VIDEO"] = 'ffpyplayer'


from kivy.lang.builder import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.properties import (
    # NumericProperty,
    ObjectProperty,
    StringProperty
)
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy import platform


Builder.load_file("player.kv")


class MenuWindow(Screen):
    pass


class WizardWindow(Screen):
    wizard_menu = ObjectProperty()
    player_widget = ObjectProperty()
    video_player = ObjectProperty()
    video_path = StringProperty()
    base_path = 'resources/videos/wizard/'
    video_list = [
        '01_fakie_gazelle.mp4',
        '02_front_gazelle.mp4',
        '03_lion_in_out.mp4',
        '04_lion_out_in.mp4',
    ]

    is_menu_visible = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self.isDesktop:
            Window.fullscreen = False
            Window.size = (414, 896)
        # self.updateSizes()

    @property
    def isDesktop(self):
        if platform in ['linux', 'win', 'macosx']:
            return True
        return False

    def updateVisibility(self):
        if self.is_menu_visible:
            self.wizard_menu.opacity = 1
            self.player_widget.opacity = 0
        else:
            self.wizard_menu.opacity = 0
            self.player_widget.opacity = 1

    def launchVideo(self, video_index):
        app.video_path = self.base_path + self.video_list[video_index]
        # self.is_menu_visible = False
        # self.updateVisibility()
        # self.video_player.state = 'play'

    def stopVideo(self):
        # self.video_player.state = 'stop'
        self.is_menu_visible = True
        self.updateVisibility()


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
    video_path = StringProperty()


if __name__ == '__main__':
    app = WheelWizardApp()
    app.run()
