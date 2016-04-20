inotifications
=================

## Notifications in ipython/jupyter notebooks

inotifications is a simple package for generating alerts or notifications in ipython/jupyter notebooks.  Notifications can be used to alert the user when a long running cell as completed, like when training a machine learning model for example.  Visual and Audio notifications are available as well as a multi-modal alerts.

## Installation
To install the most recent stable release run `pip install inotifications`.

To install the latest version run `pip install git+git://github.com/niloch/inotifications.git@master` or
`git clone https://github.com/niloch/inotifications.git` followed by `pip install -e inotifications/`

## Audio Notifications

  

```python
from inotifications import AudioNotifier

#Use one of the included sound effects "pad_confirm.wav"(default) | "fins_success-1.wav"
notifier = AudioNotifier(audio_file="pad_confirm.wav")

####  Insert Long Running Code here
#for i in range(10000):
#    for j in range(100000):
        ### perform some operation
#        pass

notifier.notify()

```

## Visual Alert


```python
from inotifications import PopupNotifier
notifier = PopupNotifier(message="The Cell is Finished!")

####  Insert Long Running Code here
#for i in range(10000):
#    for j in range(100000):
        ### perform some operation
#        pass

notifier.notify()
```

## Multi-modal Alert

```python
from inotifications import AudioPopupNotifier

#User supplied sound file with relative path to working directory
notifier = AudioPopupNotifier(message="Completed", audio_file="bell_chime.wav")

####  Insert Long Running Code here
#for i in range(10000):
#    for j in range(100000):
        ### perform some operation
#        pass

notifier.notify()

```


## Default Sounds

Included default sounds are licensed under the [:copyright: Creative Commons](http://creativecommons.org/licenses/by/3.0/us/legalcode)

* **pad_confirm.wav** via [dev_tones](http://rcptones.com/dev_tones/)
* **fins_success.wav** via [freesound.org](http://www.freesound.org/)

