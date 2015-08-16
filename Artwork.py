class ArtworkInfo(object):
	class Data(object):
		def __get__(self, instance, owner):
			return instance.artwork.data()

		def __set__(self, instance, value):
			instance.artwork.setData_(value)


	class Downloaded(object):
		def __get__(self, instance, owner):
			return instance.artwork.downloaded()


	class Format(object):
		def __get__(self, instance, owner):
			return instance.artwork.format()


	class Kind(object):
		def __get__(self, instance, owner):
			return instance.artwork.kind()

		def __set__(self, instance, value):
			instance.artwork.setKind_(value)


	class Description(object):
		def __get__(self, instance, owner):
			return instance.artwork.objectDescription()

		def __set__(self, instance, value):
			instance.artwork.setObjectDescription_(value)


	class RawData(object):
		def __get__(self, instance, owner):
			return instance.artwork.rawData()

		def __set__(self, instance, value):
			instance.artwork.setRawData_(value)


class Artwork(object):
	def __init__(self, artwork):
		self.artwork = artwork
	
	data = ArtworkInfo.Data()
	description = ArtworkInfo.Description()
	downloaded = ArtworkInfo.Downloaded()
	format = ArtworkInfo.Format()
	kind = ArtworkInfo.Kind()
	raw_data = ArtworkInfo.RawData()
