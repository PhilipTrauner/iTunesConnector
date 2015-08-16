# iTunes Connector
Abstraction layer around ScriptingBridge to control iTunes with *style*.

## Installation
Clone the repo
```
git clone https://github.com/PhilipTrauner/iTunesConnector
```

Run install script
```
python3 iTunesConnector/setup.py install
```

## Usage Example
```python
from iTunesConnector import iTunes

itunes = iTunes()

# Starting track
itunes.play()
# Get album of current track
print(itunes.current_track.album)
# Get length of current playlist
print(itunes.current_playlist.time)
# Get genre of currently highlighted tracks
for song in itunes.selection:
	print(song.genre)
# Playing 11th track of current playlist
itunes.play(itunes.current_playlist.tracks[10])
```


<<<<<<< HEAD
=======
## Todo
* ~~Play song by name~~
* ~~Playlist info~~
* ~~Fetch Album artwork~~
* ~~Editing track tags (put off for now because I can't get it to work)~~ (works now)
* Reimplement search


# Notes
Python 3 is not supported anymore because appscript has been replaced by ScriptingBridge.
iTunesConnector can be executed by a self compiled python installation in addition to the standard Python installation on OS X. 

>>>>>>> 5083421095f5c62986e1f8c9d509a186a84ca460


