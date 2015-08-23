import sys
if sys.version[:3] == "2.7":
	sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC')
from ScriptingBridge import SBApplication
from iTunesConnector.States import States
from iTunesConnector.Playlist import Playlist
from iTunesConnector.Track import Track
from iTunesConnector.AirplayDevice import AirplayDevice
from iTunesConnector.iTunes import iTunesItem
from iTunesConnector.Window import Window


class iTunesInfo(object):
	class CurrentTrack(object):
		def __get__(self, instance, owner):
			return Track(instance.itunes.currentTrack())


	class CurrentPlaylist(object):
		def __get__(self, instance, owner):
			return Playlist(instance.itunes.currentPlaylist())


	class Selection(object):
		def __get__(self, instance, owner):
			results = []
			for i in instance.itunes.selection().get():
				results.append(Track(i))
			return results


	class AirPlayDevices(object):
		def __get__(self, instance, owner):
			results = []
			for i in instance.itunes.AirPlayDevices():
				results.append(AirplayDevice(i))
			return results


	class AirPlayEnabled(object):
		def __get__(self, instance, owner):
			return instance.itunes.AirPlayEnabled()


	class EQEnabled(object):
		def __get__(self, instance, owner):
			return instance.itunes.EQEnabled()


	class EQPresets(object):
		def __get__(self, instance, owner):
			return instance.itunes.EQPresets()


	class EQWindows(object):
		def __get__(self, instance, owner):
			return instance.itunes.EQWindows()


	class BrowserWindows(object):
		def __get__(self, instance, owner):
			return instance.itunes.browserWindows()


	class Converting(object):
		def __get__(self, instance, owner):
			return instance.itunes.converting()


	class CurrentAirPlayDevices(object):
		def __get__(self, instance, owner):
			return AirplayDevice(instance.itunes.currentAirPlayDevices())

		def __set__(self, instance, value):
			instance.itunes.setCurrentAirPlayDevices_(value.airplay_device)


	class CurrentEQPreset(object):
		def __get__(self, instance, owner):
			return instance.itunes.currentEQPreset()

		def __set__(self, instance, value):
			instance.itunes.setCurrentEQPreset_(value)


	class CurrentEncoder(object):
		def __get__(self, instance, owner):
			return instance.itunes.currentEncoder()

		def __set__(self, instance, value):
			instance.itunes.setCurrentEncoder_(value)


	class CurrentStreamTitle(object):
		def __get__(self, instance, owner):
			return instance.itunes.currentStreamTitle()


	class CurrentStreamURL(object):
		def __get__(self, instance, owner):
			return instance.itunes.currentStreamURL()


	class CurrentVisual(object):
		def __get__(self, instance, owner):
			return instance.itunes.currentVisual()

		def __set__(self, instance, value):
			instance.itunes.setCurrentVisual_(value)


	class Encoders(object):
		def __get__(self, instance, owner):
			return instance.itunes.encoders()


	class FastForward(object):
		def __get__(self, instance, owner):
			return instance.itunes.fastForward()


	class FixedIndexing(object):
		def __get__(self, instance, owner):
			return instance.itunes.fixedIndexing()

		def __set__(self, instance, value):
			instance.itunes.setFixedIndexing_(value)


	class Frontmost(object):
		def __get__(self, instance, owner):
			return instance.itunes.frontmost()

		def __set__(self, instance, value):
			instance.itunes.setFrontmost_(value)


	class FullScreen(object):
		def __get__(self, instance, owner):
			return instance.itunes.fullScreen()

		def __set__(self, instance, value):
			instance.itunes.setFullScreen_(value)


	class PlayerPosition(object):
		def __get__(self, instance, owner):
			return instance.itunes.playerPosition()

		def __set__(self, instance, value):
			instance.itunes.setPlayerPosition_(value)


	class PlayerState(object):
		def __get__(self, instance, owner):
			return instance.itunes.playerState()


	class PlaylistWindows(object):
		def __get__(self, instance, owner):
			return instance.itunes.playlistWindows()


	class PrintPrintDialog(object):
		def __get__(self, instance, owner):
			return instance.itunes.printPrintDialog_withProperties_kind_theme_()


	class SoundVolume(object):
		def __get__(self, instance, owner):
			return instance.itunes.soundVolume()

		def __set__(self, instance, value):
			instance.itunes.setSoundVolume_(value)


	class Sources(object):
		def __get__(self, instance, owner):
			return instance.itunes.sources()


	class Version(object):
		def __get__(self, instance, owner):
			return instance.itunes.version()


	class VisualSize(object):
		def __get__(self, instance, owner):
			return instance.itunes.visualSize()

		def __set__(self, instance, value):
			instance.itunes.setVisualSize_(value)


	class Visuals(object):
		def __get__(self, instance, owner):
			return instance.itunes.visuals()


	class VisualsEnabled(object):
		def __get__(self, instance, owner):
			return instance.itunes.visualsEnabled()

		def __set__(self, instance, value):
			instance.itunes.setVisualsEnabled_(value)


	class Windows(object):
		def __get__(self, instance, owner):
			results = []
			for i in instance.itunes.windows():
				results.append(Window(i))
			return results

			
class iTunes(iTunesItem):
	def __init__(self):
		self.itunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
	

	def play(self, item=None):
		if item != None:
			if isinstance(item, Track):
				item.track.playOnce_(None)
			elif isinstance(item, Playlist):
				item.playlist.playOnce_(None)
			else:
				raise ValueError("Not a valid track or playlist")
		else:
			self.itunes.playpause()


	def pause(self):
		self.itunes.pause()


	def stop(self):
		self.itunes.stop()


	def resume(self):
		self.itunes.resume()


	def next(self):
		self.itunes.nextTrack()


	def back(self):
		self.itunes.previousTrack()


	def fast_forward(self):
		self.itunes.fastForward()


	def rewind(self):
		self.itunes.rewind()


	def quit(self):
		self.itunes.quit()


	def create_playlist(self, name):
		playlist = self.itunes.classForScriptingClass_("playlist").alloc().initWithProperties_({"name" : name})
		self.itunes.sources()[0].playlists().insertObject_atIndex_(playlist, 0)
		return Playlist(playlist)


	def search(self, name=None, album=None, artist=None, genre=None, loved=None):
		loved_matches = []
		if loved != None:
			for track in self.current_playlist.tracks:
				if loved:
					if track.loved:
						loved_matches.append(track)
				else:
					if not track.loved:
						loved_matches.append(track)
		else:
			loved_matches = self.current_playlist.tracks
		genre_matches = []
		if genre != None:
			for track in loved_matches:
				if genre.lower() in track.genre.lower():
					genre_matches.append(track)
		else:
			genre_matches = loved_matches
		artist_matches = []
		if artist != None:
			for track in genre_matches:
				if artist.lower() in track.artist.lower():
					artist_matches.append(track)
		else:
			artist_matches = genre_matches
		album_matches = []
		if album != None:
			for track in artist_matches:
				if album.lower() in track.album.lower():
					album_matches.append(track)
		else:
			album_matches = artist_matches
		name_matches = []
		if name != None:
			for track in album_matches:
				if name.lower() in track.name.lower():
					name_matches.append(track)
			return name_matches
		return album_matches


	playing = States.Playing()
	paused = States.Paused()
	stopped = States.Stopped()
	fast_forwarding = States.FastForward()
	rewinding = States.Rewind()
	current_track = iTunesInfo.CurrentTrack()
	current_playlist = iTunesInfo.CurrentPlaylist()
	selection = iTunesInfo.Selection()
	airplay_devices = iTunesInfo.AirPlayDevices()
	airplay_enabled = iTunesInfo.AirPlayEnabled()
	eq_enabled = iTunesInfo.EQEnabled()
	eq_presets = iTunesInfo.EQPresets()
	eq_windows = iTunesInfo.EQWindows()
	browser_windows = iTunesInfo.BrowserWindows()
	converting = iTunesInfo.Converting()
	current_airplay_devices = iTunesInfo.CurrentAirPlayDevices()
	current_eq_preset = iTunesInfo.CurrentEQPreset()
	current_encoder = iTunesInfo.CurrentEncoder()
	current_stream_title = iTunesInfo.CurrentStreamTitle()
	current_stream_url = iTunesInfo.CurrentStreamURL()
	current_visual = iTunesInfo.CurrentVisual()
	encoders = iTunesInfo.Encoders()
	fixed_indexing = iTunesInfo.FixedIndexing()
	frontmost = iTunesInfo.Frontmost()
	full_screen = iTunesInfo.FullScreen()
	player_position = iTunesInfo.PlayerPosition()
	player_state = iTunesInfo.PlayerState()
	playlist_windows = iTunesInfo.PlaylistWindows()
	print_print_dialog = iTunesInfo.PrintPrintDialog()
	sound_volume = iTunesInfo.SoundVolume()
	sources = iTunesInfo.Sources()
	version = iTunesInfo.Version()
	visual_size = iTunesInfo.VisualSize()
	visuals = iTunesInfo.Visuals()
	visuals_enabled = iTunesInfo.VisualsEnabled()
	windows = iTunesInfo.Windows()
