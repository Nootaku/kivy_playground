from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class PlayerWidget(Screen):
    return_to = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getVideoFolder(self, source):
        video_folder = source.split('/')[-2]

        self.return_to = video_folder
