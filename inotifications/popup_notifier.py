from .inotifier import Notifier
from IPython.display import display, HTML


class PopupNotifier(Notifier):
    """Show a Popup upon cell completion"""

    def __init__(self, message="Cell Completed!"):
        super(PopupNotifier, self).__init__()
        self.message = message
        self.template = '<script type="text/javascript">alert("{}");</script>'

    def notify(self):
        return display(HTML(self.template.format(self.message)))
