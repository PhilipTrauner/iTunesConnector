from iTunes import iTunesItem

class WindowInfo(object):
	class Bounds(object):
		def __get__(self, instance, owner):
			return instance.window.bounds()

		def __set__(self, instance, value):
			instance.window.setBounds_(value)


	class Closeable(object):
		def __get__(self, instance, owner):
			return instance.window.closeable()


	class Collapseable(object):
		def __get__(self, instance, owner):
			return instance.window.collapseable()


	class Collapsed(object):
		def __get__(self, instance, owner):
			return instance.window.collapsed()

		def __set__(self, instance, value):
			instance.window.setCollapsed_(value)


	class Position(object):
		def __get__(self, instance, owner):
			return instance.window.position()

		def __set__(self, instance, value):
			instance.window.setPosition_(value)


	class Resizable(object):
		def __get__(self, instance, owner):
			return instance.window.resizable()


	class Visible(object):
		def __get__(self, instance, owner):
			return instance.window.visible()

		def __set__(self, instance, value):
			instance.window.setVisible_(value)


	class Zoomable(object):
		def __get__(self, instance, owner):
			return instance.window.zoomable()


	class Zoomed(object):
		def __get__(self, instance, owner):
			return instance.window.zoomed()

		def __set__(self, instance, value):
			instance.window.setZoomed_(value)


class Window(iTunesItem):
	def __init__(self, window):
		self.window = window
		self.item = self.window


	bounds = WindowInfo.Bounds()
	closeable = WindowInfo.Closeable()
	collapseable = WindowInfo.Collapseable()
	collapsed = WindowInfo.Collapsed()
	position = WindowInfo.Position()
	resizable = WindowInfo.Resizable()
	visible = WindowInfo.Visible()
	zoomable = WindowInfo.Zoomable()
	zoomed = WindowInfo.Zoomed()