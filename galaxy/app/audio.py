from kivy.core.audio import SoundLoader


def loadAudio(self):
    """Initialize audio.
    """
    self.sound_begin = SoundLoader.load('audio/begin.wav')
    self.sound_galaxy = SoundLoader.load('audio/galaxy.wav')
    self.sound_impact = SoundLoader.load('audio/gameover_impact.wav')
    self.sound_game_over = SoundLoader.load('audio/gameover_voice.wav')
    self.sound_music = SoundLoader.load('audio/music1.wav')
    self.sound_restart = SoundLoader.load('audio/restart.wav')

    self.sound_music.volume = 1
    self.sound_begin.volume = .25
    self.sound_galaxy.volume = .25
    self.sound_game_over.volume = .25
    self.sound_restart.volume = .25
    self.sound_impact.volume = .6
