import os
os.environ["KIVY_VIDEO"] = 'ffpyplayer'


from kivy.lang.builder import Builder
from kivymd.app import MDApp

# Layouts
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout

# Components
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel

# Properties
from kivy.properties import (
    Clock,
    NumericProperty,
    ObjectProperty,
    StringProperty,
    BooleanProperty
)
from kivy.core.window import Window
from kivy import platform

# Metrics
from kivy.metrics import dp
from video_list import VIDEO_LIST


Builder.load_file("player.kv")


class MenuWindow(MDScreen):
    title = 'Wheel Wizard'
    title_dp_size = 60


class TopBar(MDBoxLayout):
    top_image = StringProperty('resources/img/icon.png')
    top_image_width = NumericProperty(.33333)
    is_logo = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = dp(90)

        Clock.schedule_once(self.updateVisuals, 0)

    def updateVisuals(self, dt):
        if self.is_logo:
            self.remove_widget(self.ids.top_bar_button)
        else:
            self.remove_widget(self.ids.top_bar_logo)


class MenuCard(MDRelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size: self.root.size


class CardButton(Button):
    card_link = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press=self.onButtonPress)
        self.background_color = (1, 1, 1, 0)

    def onButtonPress(self, instance):
        app.root.current = self.card_link


class CardLabel(MDLabel):
    card_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, .25)
        self.pos_hint = {'x': .15, 'y': .08}
        # self.color = (1, 192 / 255, 34 / 255, 1)  # Orange
        self.color = (0.6, 0.87, 0, 1)  # Green
        self.outline_color = (.28, .28, .28, 1)
        self.outline_width = 1
        self.font_size = 50
        self.font_name = 'resources/fonts/Natural.otf'


class WizardWindow(MDScreen):
    title = 'Wizard Tricks'
    title_dp_size = 45


class SlideWindow(MDScreen):
    title = 'Slide Tricks'
    title_dp_size = 45


class SlalomWindow(MDScreen):
    title = 'Slalom Tricks'
    title_dp_size = 45


class StreetWindow(MDScreen):
    title = 'Street Tricks'
    title_dp_size = 45


class VideoButton(Button):
    video_index = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = dp(65)
        self.bind(on_release=self.onButtonRelease)
        self.bind(on_press=self.playVideo)

    def onButtonRelease(self, instance):
        app.root.current = 'player'

    def playVideo(self, instance):
        self.parent.updateVideoPath(self.video_index)


class VideoList(MDGridLayout):
    video_folder = StringProperty('wizard')
    video_list = ObjectProperty(VIDEO_LIST)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.spacing = 5

        Clock.schedule_once(self.updateVideoList, 0)

    def updateVideoList(self, dt):
        app.video_folder = self.video_folder
        v_list = self.video_list[self.video_folder]

        for i in range(len(v_list)):
            button = VideoButton()
            button.video_index = i
            button.text = v_list[i]['name']
            self.add_widget(button)

    def updateVideoPath(self, video_index):
        v_list = self.video_list[self.video_folder]
        app.video_path = '/'.join(
            (
                app.video_base_path,
                self.video_folder,
                v_list[video_index]['file']
            )
        )


class MainWindow(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.isDesktop:
            Window.fullscreen = False
            Window.size = (414, 896)

    @property
    def isDesktop(self):
        if platform in ['linux', 'win', 'macosx']:
            return True
        return False


class WheelWizardApp(MDApp):
    video_path = StringProperty()
    video_base_path = StringProperty('resources/videos')
    video_folder = StringProperty()

    video_list = VIDEO_LIST

    def build(self):
        # Dark or Light theme
        self.theme_cls.theme_style = "Dark"

        # Primary color palette (for buttons)
        # self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        # self.theme_cls.primary_hue = "200"


if __name__ == '__main__':
    app = WheelWizardApp()
    app.run()
