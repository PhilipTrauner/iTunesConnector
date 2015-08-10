# iTunes Connector
Abstraction layer around appscript to control iTunes with *style*.

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
from iTunes import iTunes

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
# Searching for songs related to "Monstercat"
tracks = itunes.search(itunes.current_playlist, "Monstercat")
# Printing out results
print(tracks)
# Plaing first result
itunes.play(tracks[0])
```


## Todo
Currently only player state and track info can be fetched as well as basic player control.  
Further down in the roadmap are: 

* ~~Play song by name~~
* ~~Playlist info~~
* Fetch Album artwork 
* Editing track tags (put off for now because I can't get it to work)

## Notes
If you like **iTunes Connector** consider giving [Anshu Chimala](https://github.com/achimala) a hug.
Thanks to his project [itunes-cli](https://github.com/achimala/itunes-cli) I was able to understand appscript much faster than I would normally have.

