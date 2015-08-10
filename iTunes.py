#!/usr/bin/python

from appscript import app, k
import sys


class States(object):
	class Playing(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.playing:
				return True
			return False


	class Paused(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.paused:
				return True
			return False


	class Stopped(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.stopped:
				return True
			return False


	class FastForward(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.fast_forwarding:
				return True
			return False


	class Rewind(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.rewinding:
				return True
			return False


class PlaylistInfo(object):
	class Shuffle(object):
		def __get__(self, instance, owner):
			return instance.playlist.shuffle()


	class Name(object):
		def __get__(self, instance, owner):
			return instance.playlist.name()


	class Parent(object):
		def __get__(self, instance, owner):
			return instance.playlist.parent()


	class SharedTracks(object):
		def __get__(self, instance, owner):
			return instance.playlist.shared_tracks()


	class FileTracks(object):
		def __get__(self, instance, owner):
			return instance.playlist.file_tracks()


	class UrlTracks(object):
		def __get__(self, instance, owner):
			return instance.playlist.URL_tracks()


	class Visible(object):
		def __get__(self, instance, owner):
			return instance.playlist.visible()


	class Tracks(object):
		def __get__(self, instance, owner):
			return instance.playlist.tracks()


	class SongRepeat(object):
		def __get__(self, instance, owner):
			return instance.playlist.song_repeat()


	class SpecialKind(object):
		def __get__(self, instance, owner):
			return instance.playlist.special_kind()


	class Time(object):
		def __get__(self, instance, owner):
			return instance.playlist.time()


	class Duration(object):
		def __get__(self, instance, owner):
			return instance.playlist.duration()


	class Shared(object):
		def __get__(self, instance, owner):
			return instance.playlist.shared()


	class Smart(object):
		def __get__(self, instance, owner):
			return instance.playlist.smart()


	class Size(object):
		def __get__(self, instance, owner):
			return instance.playlist.size()


class Playlist(object):
	def __init__(self, playlist):
		self.playlist = playlist


	def __str__(self):
		return self.playlist.name()


	def __repr__(self):
		return self.playlist.name()


	shuffle = PlaylistInfo.Shuffle()
	name = PlaylistInfo.Name()
	parent = PlaylistInfo.Parent()
	shared_tracks = PlaylistInfo.SharedTracks()
	file_tracks = PlaylistInfo.FileTracks()
	URL_tracks = PlaylistInfo.UrlTracks()
	visible = PlaylistInfo.Visible()
	tracks = PlaylistInfo.Tracks()
	song_repeat = PlaylistInfo.SongRepeat()
	special_kind = PlaylistInfo.SpecialKind()
	time = PlaylistInfo.Time()
	duration = PlaylistInfo.Duration()
	shared = PlaylistInfo.Shared()
	smart = PlaylistInfo.Smart()
	size = PlaylistInfo.Size()


class ArtworkInfo(object):
	class Data(object):
		def __get__(self, instance, owner):
			return instance.artwork.data_()


	class Description(object):
		def __get__(self, instance, owner):
			return instance.artwork.description()


	class Downloaded(object):
		def __get__(self, instance, owner):
			return instance.artwork.downloaded()


	class Format(object):
		def __get__(self, instance, owner):
			return instance.artwork.format()


	class Kind(object):
		def __get__(self, instance, owner):
			return instance.artwork.kind()


	class RawData(object):
		def __get__(self, instance, owner):
			return instance.artwork.raw_data()


class Artwork(object):
	def __init__(self, artwork):
		self.artwork = artwork
	
	data = ArtworkInfo.Data()
	description = ArtworkInfo.Description()
	downloaded = ArtworkInfo.Downloaded()
	format = ArtworkInfo.Format()
	kind = ArtworkInfo.Kind()
	raw_data = ArtworkInfo.RawData()


class TrackInfo(object):
	class Name(object):
		def __get__(self, instance, owner):
			return instance.track.name()


	class Comment(object):
		def __get__(self, instance, owner):
			return instance.track.comment()


	class Rating(object):
		def __get__(self, instance, owner):
			return instance.track.rating()


	class SortComposer(object):
		def __get__(self, instance, owner):
			return instance.track.sort_composer()


	class Lyrics(object):
		def __get__(self, instance, owner):
			return instance.track.lyrics()


	class Show(object):
		def __get__(self, instance, owner):
			return instance.track.show()


	class Bpm(object):
		def __get__(self, instance, owner):
			return instance.track.bpm()


	class Unplayed(object):
		def __get__(self, instance, owner):
			return instance.track.unplayed()


	class BitRate(object):
		def __get__(self, instance, owner):
			return instance.track.bit_rate()


	class SortAlbumArtist(object):
		def __get__(self, instance, owner):
			return instance.track.sort_album_artist()


	class Composer(object):
		def __get__(self, instance, owner):
			return instance.track.composer()


	class Year(object):
		def __get__(self, instance, owner):
			return instance.track.year()


	class Duration(object):
		def __get__(self, instance, owner):
			return instance.track.duration()


	class SortShow(object):
		def __get__(self, instance, owner):
			return instance.track.sort_show()


	class PlayedDate(object):
		def __get__(self, instance, owner):
			return instance.track.played_date()


	class LongDescription(object):
		def __get__(self, instance, owner):
			return instance.track.long_description()


	class Size(object):
		def __get__(self, instance, owner):
			return instance.track.size()


	class Album(object):
		def __get__(self, instance, owner):
			return instance.track.album()


	class AlbumRatingKind(object):
		def __get__(self, instance, owner):
			return instance.track.album_rating_kind()


	class Podcast(object):
		def __get__(self, instance, owner):
			return instance.track.podcast()


	class ModificationDate(object):
		def __get__(self, instance, owner):
			return instance.track.modification_date()


	class Bookmark(object):
		def __get__(self, instance, owner):
			return instance.track.bookmark()


	class SkippedDate(object):
		def __get__(self, instance, owner):
			return instance.track.skipped_date()


	class DiscNumber(object):
		def __get__(self, instance, owner):
			return instance.track.disc_number()


	class Start(object):
		def __get__(self, instance, owner):
			return instance.track.start()


	class DatabaseId(object):
		def __get__(self, instance, owner):
			return instance.track.database_ID()


	class Shufflable(object):
		def __get__(self, instance, owner):
			return instance.track.shufflable()


	class Location(object):
		def __get__(self, instance, owner):
			return instance.track.location()


	class Gapless(object):
		def __get__(self, instance, owner):
			return instance.track.gapless()


	class SortAlbum(object):
		def __get__(self, instance, owner):
			return instance.track.sort_album()


	class SeasonNumber(object):
		def __get__(self, instance, owner):
			return instance.track.season_number()


	class SkippedCount(object):
		def __get__(self, instance, owner):
			return instance.track.skipped_count()


	class VolumeAdjustment(object):
		def __get__(self, instance, owner):
			return instance.track.volume_adjustment()


	class Category(object):
		def __get__(self, instance, owner):
			return instance.track.category()


	class Finish(object):
		def __get__(self, instance, owner):
			return instance.track.finish()


	class Bookmarkable(object):
		def __get__(self, instance, owner):
			return instance.track.bookmarkable()


	class Description(object):
		def __get__(self, instance, owner):
			return instance.track.description()


	class Compilation(object):
		def __get__(self, instance, owner):
			return instance.track.compilation()


	class RatingKind(object):
		def __get__(self, instance, owner):
			return instance.track.rating_kind()


	class EpisodeId(object):
		def __get__(self, instance, owner):
			return instance.track.episode_ID()


	class TrackNumber(object):
		def __get__(self, instance, owner):
			return instance.track.track_number()


	class Genre(object):
		def __get__(self, instance, owner):
			return instance.track.genre()


	class DateAdded(object):
		def __get__(self, instance, owner):
			return instance.track.date_added()


	class EpisodeNumber(object):
		def __get__(self, instance, owner):
			return instance.track.episode_number()


	class Eq(object):
		def __get__(self, instance, owner):
			return instance.track.EQ()


	class AlbumArtist(object):
		def __get__(self, instance, owner):
			return instance.track.album_artist()


	class Kind(object):
		def __get__(self, instance, owner):
			return instance.track.kind()


	class DiscCount(object):
		def __get__(self, instance, owner):
			return instance.track.disc_count()


	class Artist(object):
		def __get__(self, instance, owner):
			return instance.track.artist()


	class ReleaseDate(object):
		def __get__(self, instance, owner):
			return instance.track.release_date()


	class Enabled(object):
		def __get__(self, instance, owner):
			return instance.track.enabled()


	class SortArtist(object):
		def __get__(self, instance, owner):
			return instance.track.sort_artist()


	class SortName(object):
		def __get__(self, instance, owner):
			return instance.track.sort_name()


	class VideoKind(object):
		def __get__(self, instance, owner):
			return instance.track.video_kind()


	class SampleRate(object):
		def __get__(self, instance, owner):
			return instance.track.sample_rate()


	class PlayedCount(object):
		def __get__(self, instance, owner):
			return instance.track.played_count()


	class Time(object):
		def __get__(self, instance, owner):
			return instance.track.time()


	class TrackCount(object):
		def __get__(self, instance, owner):
			return instance.track.track_count()


	class AlbumRating(object):
		def __get__(self, instance, owner):
			return instance.track.album_rating()


	class Grouping(object):
		def __get__(self, instance, owner):
			return instance.track.grouping()


	class Artworks(object):
		def __get__(self, instance, owner):
			artworks = []
			for i in instance.track.artworks():
				artworks.append(Artwork(i))
			return artworks


class Track(object):
	def __init__(self, track):
		self.track = track


	def __str__(self):
		return self.track.name()


	def __repr__(self):
		return self.track.name() + " - " + self.track.artist() + " - " + self.track.album()

	name = TrackInfo.Name()
	comment = TrackInfo.Comment()
	rating = TrackInfo.Rating()
	sort_composer = TrackInfo.SortComposer()
	lyrics = TrackInfo.Lyrics()
	show = TrackInfo.Show()
	bpm = TrackInfo.Bpm()
	unplayed = TrackInfo.Unplayed()
	bit_rate = TrackInfo.BitRate()
	sort_album_artist = TrackInfo.SortAlbumArtist()
	composer = TrackInfo.Composer()
	year = TrackInfo.Year()
	duration = TrackInfo.Duration()
	sort_show = TrackInfo.SortShow()
	played_date = TrackInfo.PlayedDate()
	long_description = TrackInfo.LongDescription()
	size = TrackInfo.Size()
	album = TrackInfo.Album()
	album_rating_kind = TrackInfo.AlbumRatingKind()
	podcast = TrackInfo.Podcast()
	modification_date = TrackInfo.ModificationDate()
	bookmark = TrackInfo.Bookmark()
	skipped_date = TrackInfo.SkippedDate()
	disc_number = TrackInfo.DiscNumber()
	start = TrackInfo.Start()
	database_ID = TrackInfo.DatabaseId()
	shufflable = TrackInfo.Shufflable()
	location = TrackInfo.Location()
	gapless = TrackInfo.Gapless()
	sort_album = TrackInfo.SortAlbum()
	season_number = TrackInfo.SeasonNumber()
	skipped_count = TrackInfo.SkippedCount()
	volume_adjustment = TrackInfo.VolumeAdjustment()
	category = TrackInfo.Category()
	finish = TrackInfo.Finish()
	bookmarkable = TrackInfo.Bookmarkable()
	description = TrackInfo.Description()
	compilation = TrackInfo.Compilation()
	rating_kind = TrackInfo.RatingKind()
	episode_ID = TrackInfo.EpisodeId()
	track_number = TrackInfo.TrackNumber()
	genre = TrackInfo.Genre()
	date_added = TrackInfo.DateAdded()
	episode_number = TrackInfo.EpisodeNumber()
	EQ = TrackInfo.Eq()
	album_artist = TrackInfo.AlbumArtist()
	kind = TrackInfo.Kind()
	disc_count = TrackInfo.DiscCount()
	artist = TrackInfo.Artist()
	release_date = TrackInfo.ReleaseDate()
	enabled = TrackInfo.Enabled()
	sort_artist = TrackInfo.SortArtist()
	sort_name = TrackInfo.SortName()
	video_kind = TrackInfo.VideoKind()
	sample_rate = TrackInfo.SampleRate()
	played_count = TrackInfo.PlayedCount()
	time = TrackInfo.Time()
	track_count = TrackInfo.TrackCount()
	album_rating = TrackInfo.AlbumRating()
	grouping = TrackInfo.Grouping()
	artworks = TrackInfo.Artworks()


class Info(object):
	class CurrentTrack(object):
		def __get__(self, instance, owner):
			return Track(instance.itunes.current_track())


	class CurrentPlaylist(object):
		def __get__(self, instance, owner):
			return Playlist(instance.itunes.current_playlist())


	class Selection(object):
		def __get__(self, instance, owner):
			results = []
			for i in instance.itunes.selection():
				results.append(Track(i))
			return results


class iTunes(object):
	def __init__(self):
		self.itunes = app("iTunes")
	
	def play(self, item=None):
		if item:
			if isinstance(item, sys.modules[__name__].Track):
				self.itunes.play(item.track)
			elif isinstance(item, sys.modules[__name__].Playlist):
				self.itunes.play(item.playlist)
			else:
				raise ValueError("Not a valid track or playlist")
		else:
			self.itunes.play()


	def pause(self):
		self.itunes.pause()


	def stop(self):
		self.itunes.stop()


	def resume(self):
		self.itunes.resume()


	def next(self):
		self.itunes.next_track()


	def back(self):
		self.itunes.back_track()


	def fast_forward(self):
		self.itunes.fast_forward()


	def rewind(self):
		self.itunes.rewind()


	def quit(self):
		self.itunes.quit()



	def search(self, playlist, key):
		results = self.itunes.search(playlist.playlist, for_=key)
		for i in range(len(results)):
			results[i] = Track(results[i])
		return results


	playing = States.Playing()
	paused = States.Paused()
	stopped = States.Stopped()
	fast_forwarding = States.FastForward()
	rewinding = States.Rewind()
	current_track = Info.CurrentTrack()
	current_playlist = Info.CurrentPlaylist()
	selection = Info.Selection()