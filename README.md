# iTunes Connector
Abstraction layer around ScriptingBridge to control iTunes with *style*.

## Installation
Clone the repo
```
git clone https://github.com/PhilipTrauner/iTunesConnector
```

Navigate into cloned repo
```
cd iTunesConnector
``` 

Run install script
```
python setup.py install
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



