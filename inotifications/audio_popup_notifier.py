from inotifier import Notifier
from IPython.display import display, Audio, HTML

import pkg_resources
import time


class AudioPopupNotifier(Notifier):
    """Play Sound and show Popup upon cell completion"""

    def __init__(self, message="Cell Completed", audio_file="pad_confirm.wav"):
        super(AudioPopupNotifier, self).__init__()
        self.message = message
        self.audio_file = audio_file
        try:
            self.audio = pkg_resources.resource_string('inotifications', 'sounds/{}'.format(audio_file))
        except IOError:
            self.audio = audio_file

        self.template = '<script type="text/javascript">alert("{}");</script>'

    def notify(self):
        display(Audio(self.audio, autoplay=True))
        time.sleep(3)
        display(HTML(self.template.format(self.message)))
