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

## Usage 
```python
from iTunes import iTunes

itunes = iTunes()

# Starting track
itunes.player.playing = True
# Get track name
print(itunes.track.name)
# Get track album
print(itunes.track.album)
# Get track artist
print(itunes.track.artist)
# Get track rating
print(itunes.track.rating)
# Skipping track
itunes.player.next()
# Previous track
itunes.player.back()
# Resuming track
itunes.player.paused = False
# Stopping track
itunes.player.stopped = True
```


## Todo
Currently only player state and track info can be fetched as well as basic player control.  
Further down in the roadmap are: 

* Play song by name
* Playlist info
* Fetch Album artwork 

## Notes
If you like **iTunes Connector** consider giving [Anshu Chimala](https://github.com/achimala) a hug.
Thanks to his project [itunes-cli](https://github.com/achimala/itunes-cli) I was able to understand appscript much faster than I would normally have.
