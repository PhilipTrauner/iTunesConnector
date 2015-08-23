class iTunesItemInfo(object):
	class Name(object):
		def __get__(self, instance, owner):
			return instance.item.name()

		def __set__(self, instance, value):
			instance.item.setName_(value)


class iTunesItem(object):
	def __init__(self, item):
		self.item = item


	def __repr__(self):
		return self.item.name()


	def __str__(self):
		return self.item.name()


	def delete(self):
		self.item.delete()

	name = iTunesItemInfo.Name()