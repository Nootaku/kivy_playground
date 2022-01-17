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
    NumericProperty,
    ObjectProperty,
    StringProperty
)
from kivy.core.window import Window
from kivy import platform

# Metrics
from kivy.metrics import dp


Builder.load_file("player.kv")


class MenuWindow(MDScreen):
    title = 'Wheel Wizard'
    title_dp_size = 60


class TopBar(MDBoxLayout):
    top_image = StringProperty('resources/img/icon.png')
    top_image_width = NumericProperty(.33333)


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

    def launchVideo(self, video_index):
        app.video_path = self.base_path + self.video_list[video_index]
        # self.video_player.state = 'play'

    def stopVideo(self):
        # self.video_player.state = 'stop'
        self.is_menu_visible = True
        self.updateVisibility()


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
        self.parent.parent.parent.launchVideo(self.video_index)


class VideoList(MDGridLayout):
    video_list = [
        'Fakie Gazelle',
        'Front Gazelle',
        'Lion In-Out',
        'Lion Out-In',
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.spacing = 5

        for i in range(len(self.video_list)):
            button = VideoButton()
            button.video_index = i
            button.text = self.video_list[i]
            self.add_widget(button)


class SlideWindow(MDScreen):
    title = 'Slide Tricks'
    title_dp_size = 45
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


class WheelWizardApp(MDApp):
    video_path = StringProperty()

    def build(self):
        # Dark or Light theme
        self.theme_cls.theme_style = "Dark"

        # Primary color palette (for buttons)
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        self.theme_cls.primary_hue = "200"


if __name__ == '__main__':
    app = WheelWizardApp()
    app.run()
    app.run()
