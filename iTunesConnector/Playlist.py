from iTunes import iTunesItem
from Track import Track


class PlaylistInfo(object):
	class Duration(object):
		def __get__(self, instance, owner):
			return instance.playlist.duration()


	class Loved(object):
		def __get__(self, instance, owner):
			return instance.playlist.loved()

		def __set__(self, instance, value):
			instance.playlist.setLoved_(value)


	class Parent(object):
		def __get__(self, instance, owner):
			return instance.playlist.parent()


	class Shuffle(object):
		def __get__(self, instance, owner):
			return instance.playlist.shuffle()

		def __set__(self, instance, value):
			instance.playlist.setShuffle_(value)


	class Size(object):
		def __get__(self, instance, owner):
			return instance.playlist.size()


	class SongRepeat(object):
		def __get__(self, instance, owner):
			return instance.playlist.songRepeat()

		def __set__(self, instance, value):
			instance.playlist.setSongRepeat_(value)


	class SpecialKind(object):
		def __get__(self, instance, owner):
			return instance.playlist.specialKind()


	class Time(object):
		def __get__(self, instance, owner):
			return instance.playlist.time()


	class Tracks(object):
		def __get__(self, instance, owner):
			results = []
			for i in instance.playlist.tracks():
				results.append(Track(i))
			return results


	class Visible(object):
		def __get__(self, instance, owner):
			return instance.playlist.visible()


class Playlist(iTunesItem):
	def __init__(self, playlist):
		self.playlist = playlist
		self.item = self.playlist


	def __repr__(self):
		return unicode("%s - %s tracks" % (self.playlist.name(), str(len(self.playlist.tracks())))).encode("utf-8")


	def add_track(self, track):
		track.add_to_playlist(self)


	duration = PlaylistInfo.Duration()
	loved = PlaylistInfo.Loved()
	parent = PlaylistInfo.Parent()
	shuffle = PlaylistInfo.Shuffle()
	size = PlaylistInfo.Size()
	song_repeat = PlaylistInfo.SongRepeat()
	special_kind = PlaylistInfo.SpecialKind()
	time = PlaylistInfo.Time()
	tracks = PlaylistInfo.Tracks()
	visible = PlaylistInfo.Visible()