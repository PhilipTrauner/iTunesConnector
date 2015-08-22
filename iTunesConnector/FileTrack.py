from Track import Track


class FileTrackInfo(object):
	class Location(object):
		def __get__(self, instance, owner):
			return instance.file_track.location()

		def __set__(self, instance, value):
			instance.setLocation_(value)


class FileTrack(Track):
	def __init__(self, file_track):
		self.track = track
		self.item = self.track


	def refresh(self):
		self.file_track.refresh()


	location = FileTrackInfo.Location()