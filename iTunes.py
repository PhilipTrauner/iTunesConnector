#!/usr/bin/python

from appscript import app, k


class States(object):
	class Playing(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.playing:
				return True
			return False


		def __set__(self, instance, value):
			if value:
				instance.itunes.play()
			else:
				instance.itunes.pause()


	class Paused(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.paused:
				return True
			return False


		def __set__(self, instance, value):
			if value:
				instance.itunes.pause()
			else:
				instance.itunes.play()


	class Stopped(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.stopped:
				return True
			return False


		def __set__(self, instance, value):
			if value:
				instance.itunes.stop()
			else:
				instance.itunes.play()


	class FastForward(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.fast_forwarding:
				return True
			return False

		def __set__(self, instance, value):
			if value:
				instance.itunes.fast_forward()
			else:
				instance.itunes.resume()

	class Rewind(object):
		def __get__(self, instance, owner):
			if instance.itunes.player_state() == k.rewinding:
				return True
			return False

		def __set__(self, instance, value):
			if value:
				instance.itunes.rewind()
			else:
				instance.itunes.resume()


class Info(object):
	class Name(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().name()


	class Comment(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().comment()


	class Rating(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().rating()


	class SortComposer(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().sort_composer()


	class Lyrics(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().lyrics()


	class Show(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().show()


	class Bpm(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().bpm()


	class Unplayed(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().unplayed()


	class BitRate(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().bit_rate()


	class SortAlbumArtist(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().sort_album_artist()


	class Composer(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().composer()


	class Year(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().year()


	class Duration(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().duration()


	class SortShow(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().sort_show()


	class PlayedDate(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().played_date()


	class LongDescription(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().long_description()


	class Size(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().size()


	class Album(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().album()


	class AlbumRatingKind(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().album_rating_kind()


	class Podcast(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().podcast()


	class ModificationDate(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().modification_date()


	class Bookmark(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().bookmark()


	class SkippedDate(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().skipped_date()


	class DiscNumber(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().disc_number()


	class Start(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().start()


	class DatabaseId(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().database_ID()


	class Shufflable(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().shufflable()


	class Location(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().location()


	class Gapless(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().gapless()


	class SortAlbum(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().sort_album()


	class SeasonNumber(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().season_number()


	class SkippedCount(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().skipped_count()


	class VolumeAdjustment(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().volume_adjustment()


	class Category(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().category()


	class Finish(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().finish()


	class Bookmarkable(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().bookmarkable()


	class Description(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().description()


	class Compilation(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().compilation()


	class RatingKind(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().rating_kind()


	class EpisodeId(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().episode_ID()


	class TrackNumber(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().track_number()


	class Genre(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().genre()


	class DateAdded(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().date_added()


	class EpisodeNumber(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().episode_number()


	class Eq(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().EQ()


	class AlbumArtist(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().album_artist()


	class Kind(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().kind()


	class DiscCount(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().disc_count()


	class Artist(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().artist()


	class ReleaseDate(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().release_date()


	class Enabled(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().enabled()


	class SortArtist(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().sort_artist()


	class SortName(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().sort_name()


	class VideoKind(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().video_kind()


	class SampleRate(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().sample_rate()


	class PlayedCount(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().played_count()


	class Time(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().time()


	class TrackCount(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().track_count()


	class AlbumRating(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().album_rating()


	class Grouping(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().grouping()


class Player(object):
	def __init__(self, itunes):
		self.itunes = itunes


	def next(self):
		self.itunes.next_track()


	def back(self):
		self.itunes.back_track()


	def quit(self):
		self.itunes.quit()


	def resume(self):
		self.itunes.resume()


	playing = States.Playing()
	paused = States.Paused()
	stopped = States.Stopped()
	fast_forwarding = States.FastForward()
	rewinding = States.Rewind()


class Track(object):
	def __init__(self, itunes):
		self.itunes = itunes


	name = Info.Name()
	comment = Info.Comment()
	rating = Info.Rating()
	sort_composer = Info.SortComposer()
	lyrics = Info.Lyrics()
	show = Info.Show()
	bpm = Info.Bpm()
	unplayed = Info.Unplayed()
	bit_rate = Info.BitRate()
	sort_album_artist = Info.SortAlbumArtist()
	composer = Info.Composer()
	year = Info.Year()
	duration = Info.Duration()
	sort_show = Info.SortShow()
	played_date = Info.PlayedDate()
	long_description = Info.LongDescription()
	size = Info.Size()
	album = Info.Album()
	album_rating_kind = Info.AlbumRatingKind()
	podcast = Info.Podcast()
	modification_date = Info.ModificationDate()
	bookmark = Info.Bookmark()
	skipped_date = Info.SkippedDate()
	disc_number = Info.DiscNumber()
	start = Info.Start()
	database_ID = Info.DatabaseId()
	shufflable = Info.Shufflable()
	location = Info.Location()
	gapless = Info.Gapless()
	sort_album = Info.SortAlbum()
	season_number = Info.SeasonNumber()
	skipped_count = Info.SkippedCount()
	volume_adjustment = Info.VolumeAdjustment()
	category = Info.Category()
	finish = Info.Finish()
	bookmarkable = Info.Bookmarkable()
	description = Info.Description()
	compilation = Info.Compilation()
	rating_kind = Info.RatingKind()
	episode_ID = Info.EpisodeId()
	track_number = Info.TrackNumber()
	genre = Info.Genre()
	date_added = Info.DateAdded()
	episode_number = Info.EpisodeNumber()
	EQ = Info.Eq()
	album_artist = Info.AlbumArtist()
	kind = Info.Kind()
	disc_count = Info.DiscCount()
	artist = Info.Artist()
	release_date = Info.ReleaseDate()
	enabled = Info.Enabled()
	sort_artist = Info.SortArtist()
	sort_name = Info.SortName()
	video_kind = Info.VideoKind()
	sample_rate = Info.SampleRate()
	played_count = Info.PlayedCount()
	time = Info.Time()
	track_count = Info.TrackCount()
	album_rating = Info.AlbumRating()
	grouping = Info.Grouping()


class iTunes(object):
	itunes = app("iTunes")
	player = Player(itunes)
	track = Track(itunes)