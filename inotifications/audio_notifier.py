from .inotifier import Notifier
from IPython.display import Audio
import os


DEAFAULT_SOUNDS_DIR = os.path.join(os.path.dirname(__file__), 'sounds')


class AudioNotifier(Notifier):
    """Play a Sound upon cell completion"""

    def __init__(self, audio_file='pad_confirm.wav'):
        super(AudioNotifier, self).__init__()
        if os.path.isfile(os.path.join(DEAFAULT_SOUNDS_DIR, audio_file)):
            self.audio_file = os.path.join(DEAFAULT_SOUNDS_DIR, audio_file)
        elif os.path.isfile(audio_file):
            self.audio_file = audio_file
        else:
            raise IOError("Audio file not found")
        self._notification = Audio(self.audio_file, autoplay=True)

    def notify(self):
        return self._notification
