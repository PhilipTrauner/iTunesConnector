from iTunesConnector.iTunes import iTunesItem
from iTunesConnector.Artwork import Artwork

class TrackInfo(object):
	class EQ(object):
		def __get__(self, instance, owner):
			return instance.track.EQ()


	class Album(object):
		def __get__(self, instance, owner):
			return instance.track.album()

		def __set__(self, instance, value):
			instance.track.setAlbum_(value)


	class AlbumArtist(object):
		def __get__(self, instance, owner):
			return instance.track.albumArtist()

		def __set__(self, instance, value):
			instance.track.setAlbumArtist_(value)


	class AlbumLoved(object):
		def __get__(self, instance, owner):
			return instance.track.albumLoved()

		def __set__(self, instance, value):
			instance.track.setAlbumLoved_(value)


	class AlbumRating(object):
		def __get__(self, instance, owner):
			return instance.track.albumRating()

		def __set__(self, instance, value):
			instance.track.setAlbumRating_(value)


	class AlbumRatingKind(object):
		def __get__(self, instance, owner):
			return instance.track.albumRatingKind()


	class Artist(object):
		def __get__(self, instance, owner):
			return instance.track.artist()

		def __set__(self, instance, value):
			instance.track.setArtist_(value)


	class Artworks(object):
		def __get__(self, instance, owner):
			artworks = []
			for i in instance.track.artworks():
				artworks.append(Artwork(i))
			return artworks


	class BitRate(object):
		def __get__(self, instance, owner):
			return instance.track.bitRate()


	class Bookmark(object):
		def __get__(self, instance, owner):
			return instance.track.bookmark()

		def __set__(self, instance, value):
			instance.track.setBookmark_(value)


	class Bookmarkable(object):
		def __get__(self, instance, owner):
			return instance.track.bookmarkable()

		def __set__(self, instance, value):
			instance.track.setBookmarkable_(value)


	class Bpm(object):
		def __get__(self, instance, owner):
			return instance.track.bpm()

		def __set__(self, instance, value):
			instance.track.setBpm_(value)


	class Category(object):
		def __get__(self, instance, owner):
			return instance.track.category()

		def __set__(self, instance, value):
			instance.track.setCategory_(value)


	class Comment(object):
		def __get__(self, instance, owner):
			return instance.track.comment()

		def __set__(self, instance, value):
			instance.track.setComment_(value)


	class Compilation(object):
		def __get__(self, instance, owner):
			return instance.track.compilation()

		def __set__(self, instance, value):
			instance.track.setCompilation_(value)


	class Composer(object):
		def __get__(self, instance, owner):
			return instance.track.composer()

		def __set__(self, instance, value):
			instance.track.setComposer_(value)


	class DatabaseID(object):
		def __get__(self, instance, owner):
			return instance.track.databaseID()


	class DateAdded(object):
		def __get__(self, instance, owner):
			return instance.track.dateAdded()


	class DiscCount(object):
		def __get__(self, instance, owner):
			return instance.track.discCount()

		def __set__(self, instance, value):
			instance.track.setDiscCount_(value)


	class DiscNumber(object):
		def __get__(self, instance, owner):
			return instance.track.discNumber()

		def __set__(self, instance, value):
			instance.track.setDiscNumber_(value)


	class Duration(object):
		def __get__(self, instance, owner):
			return instance.track.duration()


	class Enabled(object):
		def __get__(self, instance, owner):
			return instance.track.enabled()

		def __set__(self, instance, value):
			instance.track.setEnabled_(value)


	class EpisodeID(object):
		def __get__(self, instance, owner):
			return instance.track.episodeID()

		def __set__(self, instance, value):
			instance.track.setEpisodeID_(value)


	class EpisodeNumber(object):
		def __get__(self, instance, owner):
			return instance.track.episodeNumber()

		def __set__(self, instance, value):
			instance.track.setEpisodeNumber_(value)


	class Finish(object):
		def __get__(self, instance, owner):
			return instance.track.finish()

		def __set__(self, instance, value):
			instance.track.setFinish_(value)


	class Gapless(object):
		def __get__(self, instance, owner):
			return instance.track.gapless()

		def __set__(self, instance, value):
			instance.track.setGapless_(value)


	class Genre(object):
		def __get__(self, instance, owner):
			return instance.track.genre()

		def __set__(self, instance, value):
			instance.track.setGenre_(value)


	class Grouping(object):
		def __get__(self, instance, owner):
			return instance.track.grouping()

		def __set__(self, instance, value):
			instance.track.setGrouping_(value)


	class ITunesU(object):
		def __get__(self, instance, owner):
			return instance.track.iTunesU()


	class Kind(object):
		def __get__(self, instance, owner):
			return instance.track.kind()


	class LongDescription(object):
		def __get__(self, instance, owner):
			return instance.track.longDescription()

		def __set__(self, instance, value):
			instance.track.setLongDescription_(value)


	class Loved(object):
		def __get__(self, instance, owner):
			return instance.track.loved()

		def __set__(self, instance, value):
			instance.track.setLoved_(value)


	class Lyrics(object):
		def __get__(self, instance, owner):
			return instance.track.lyrics()

		def __set__(self, instance, value):
			instance.track.setLyrics_(value)


	class ModificationDate(object):
		def __get__(self, instance, owner):
			return instance.track.modificationDate()


	class ObjectDescription(object):
		def __get__(self, instance, owner):
			return instance.track.objectDescription()

		def __set__(self, instance, value):
			instance.track.setObjectDescription_(value)


	class PlayedCount(object):
		def __get__(self, instance, owner):
			return instance.track.playedCount()

		def __set__(self, instance, value):
			instance.track.setPlayedCount_(value)


	class PlayedDate(object):
		def __get__(self, instance, owner):
			return instance.track.playedDate()

		def __set__(self, instance, value):
			instance.track.setPlayedDate_(value)


	class Podcast(object):
		def __get__(self, instance, owner):
			return instance.track.podcast()


	class Rating(object):
		def __get__(self, instance, owner):
			return instance.track.rating()

		def __set__(self, instance, value):
			instance.track.setRating_(value)


	class RatingKind(object):
		def __get__(self, instance, owner):
			return instance.track.ratingKind()


	class ReleaseDate(object):
		def __get__(self, instance, owner):
			return instance.track.releaseDate()


	class SampleRate(object):
		def __get__(self, instance, owner):
			return instance.track.sampleRate()


	class SeasonNumber(object):
		def __get__(self, instance, owner):
			return instance.track.seasonNumber()

		def __set__(self, instance, value):
			instance.track.setSeasonNumber_(value)


	class Show(object):
		def __get__(self, instance, owner):
			return instance.track.show()

		def __set__(self, instance, value):
			instance.track.setShow_(value)


	class Shufflable(object):
		def __get__(self, instance, owner):
			return instance.track.shufflable()

		def __set__(self, instance, value):
			instance.track.setShufflable_(value)


	class Size(object):
		def __get__(self, instance, owner):
			return instance.track.size()


	class SkippedCount(object):
		def __get__(self, instance, owner):
			return instance.track.skippedCount()

		def __set__(self, instance, value):
			instance.track.setSkippedCount_(value)


	class SkippedDate(object):
		def __get__(self, instance, owner):
			return instance.track.skippedDate()

		def __set__(self, instance, value):
			instance.track.setSkippedDate_(value)


	class SortAlbum(object):
		def __get__(self, instance, owner):
			return instance.track.sortAlbum()

		def __set__(self, instance, value):
			instance.track.setSortAlbum_(value)


	class SortAlbumArtist(object):
		def __get__(self, instance, owner):
			return instance.track.sortAlbumArtist()

		def __set__(self, instance, value):
			instance.track.setSortAlbumArtist_(value)


	class SortArtist(object):
		def __get__(self, instance, owner):
			return instance.track.sortArtist()

		def __set__(self, instance, value):
			instance.track.setSortArtist_(value)


	class SortComposer(object):
		def __get__(self, instance, owner):
			return instance.track.sortComposer()

		def __set__(self, instance, value):
			instance.track.setSortComposer_(value)


	class SortName(object):
		def __get__(self, instance, owner):
			return instance.track.sortName()

		def __set__(self, instance, value):
			instance.track.setSortName_(value)


	class SortShow(object):
		def __get__(self, instance, owner):
			return instance.track.sortShow()

		def __set__(self, instance, value):
			instance.track.setSortShow_(value)


	class Start(object):
		def __get__(self, instance, owner):
			return instance.track.start()

		def __set__(self, instance, value):
			instance.track.setStart_(value)


	class Time(object):
		def __get__(self, instance, owner):
			return instance.track.time()


	class TrackCount(object):
		def __get__(self, instance, owner):
			return instance.track.trackCount()

		def __set__(self, instance, value):
			instance.track.setTrackCount_(value)


	class TrackNumber(object):
		def __get__(self, instance, owner):
			return instance.track.trackNumber()

		def __set__(self, instance, value):
			instance.track.setTrackNumber_(value)


	class Unplayed(object):
		def __get__(self, instance, owner):
			return instance.track.unplayed()

		def __set__(self, instance, value):
			instance.track.setUnplayed_(value)


	class VideoKind(object):
		def __get__(self, instance, owner):
			return instance.track.videoKind()

		def __set__(self, instance, value):
			instance.track.setVideoKind_(value)


	class VolumeAdjustment(object):
		def __get__(self, instance, owner):
			return instance.track.volumeAdjustment()

		def __set__(self, instance, value):
			instance.track.setVolumeAdjustment_(value)


	class Year(object):
		def __get__(self, instance, owner):
			return instance.track.year()

		def __set__(self, instance, value):
			instance.track.setYear_(value)


class Track(iTunesItem):
	def __init__(self, track):
		self.track = track
		self.item = self.track


	def __repr__(self):
		return "%s - %s" % (self.track.name(), self.track.artist())


	def add_to_playlist(self, playlist):
		self.track.duplicateTo_(playlist.playlist)


	eq = TrackInfo.EQ()
	album = TrackInfo.Album()
	album_artist = TrackInfo.AlbumArtist()
	album_loved = TrackInfo.AlbumLoved()
	album_rating = TrackInfo.AlbumRating()
	album_rating_kind = TrackInfo.AlbumRatingKind()
	artist = TrackInfo.Artist()
	artworks = TrackInfo.Artworks()
	bit_rate = TrackInfo.BitRate()
	bookmark = TrackInfo.Bookmark()
	bookmarkable = TrackInfo.Bookmarkable()
	bpm = TrackInfo.Bpm()
	category = TrackInfo.Category()
	comment = TrackInfo.Comment()
	compilation = TrackInfo.Compilation()
	composer = TrackInfo.Composer()
	database_id = TrackInfo.DatabaseID()
	date_added = TrackInfo.DateAdded()
	disc_count = TrackInfo.DiscCount()
	disc_number = TrackInfo.DiscNumber()
	duration = TrackInfo.Duration()
	enabled = TrackInfo.Enabled()
	episode_id = TrackInfo.EpisodeID()
	episode_number = TrackInfo.EpisodeNumber()
	finish = TrackInfo.Finish()
	gapless = TrackInfo.Gapless()
	genre = TrackInfo.Genre()
	grouping = TrackInfo.Grouping()
	itunes_u = TrackInfo.ITunesU()
	kind = TrackInfo.Kind()
	long_description = TrackInfo.LongDescription()
	loved = TrackInfo.Loved()
	lyrics = TrackInfo.Lyrics()
	modification_date = TrackInfo.ModificationDate()
	object_description = TrackInfo.ObjectDescription()
	played_count = TrackInfo.PlayedCount()
	played_date = TrackInfo.PlayedDate()
	podcast = TrackInfo.Podcast()
	rating = TrackInfo.Rating()
	rating_kind = TrackInfo.RatingKind()
	release_date = TrackInfo.ReleaseDate()
	sample_rate = TrackInfo.SampleRate()
	season_number = TrackInfo.SeasonNumber()
	show = TrackInfo.Show()
	shufflable = TrackInfo.Shufflable()
	size = TrackInfo.Size()
	skipped_count = TrackInfo.SkippedCount()
	skipped_date = TrackInfo.SkippedDate()
	sort_album = TrackInfo.SortAlbum()
	sort_album_artist = TrackInfo.SortAlbumArtist()
	sort_artist = TrackInfo.SortArtist()
	sort_composer = TrackInfo.SortComposer()
	sort_name = TrackInfo.SortName()
	sort_show = TrackInfo.SortShow()
	start = TrackInfo.Start()
	time = TrackInfo.Time()
	track_count = TrackInfo.TrackCount()
	track_number = TrackInfo.TrackNumber()
	unplayed = TrackInfo.Unplayed()
	video_kind = TrackInfo.VideoKind()
	volume_adjustment = TrackInfo.VolumeAdjustment()
	year = TrackInfo.Year()
