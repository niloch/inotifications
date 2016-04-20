from abc import ABCMeta, abstractmethod
from exceptions import NotImplementedError


class Notifier(object):
    """IPython Notifier"""

    __metaclass__ = ABCMeta

    def __init__(self):
        super(Notifier, self).__init__()

    @abstractmethod
    def notify(self):
        return NotImplementedError()
