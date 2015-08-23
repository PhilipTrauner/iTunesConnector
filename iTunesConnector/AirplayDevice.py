from iTunesConnector.iTunes import iTunesItem

class AirplayDeviceInfo(object):
	class Active(object):
		def __get__(self, instance, owner):
			return instance.airplay_device.active()


	class Available(object):
		def __get__(self, instance, owner):
			return instance.airplay_device.available()


	class Kind(object):
		def __get__(self, instance, owner):
			return instance.airplay_device.kind()


	class NetworkAddress(object):
		def __get__(self, instance, owner):
			return instance.airplay_device.networkAddress()


	class Protected(object):
		def __get__(self, instance, owner):
			return instance.airplay_device.protected()


	class Selected(object):
		def __get__(self, instance, owner):
			return instance.airplay_device.selected()

		def __set__(self, instance, value):
			instance.airplay_device.setSelected_(value)


	class SoundVolume(object):
		def __get__(self, instance, owner):
			return instance.airplay_device.soundVolume()

		def __set__(self, instance, value):
			instance.airplay_device.setSoundVolume_(value)


	class SupportsAudio(object):
		def __get__(self, instance, owner):
			return instance.airplay_device.supportsAudio()


	class SupportsVideo(object):
		def __get__(self, instance, owner):
			return instance.airplay_device.supportsVideo()


class AirplayDevice(iTunesItem):
	def __init__(self, airplay_device):
		self.airplay_device = airplay_device
		self.item = self.airplay_device
		

	active = AirplayDeviceInfo.Active()
	available = AirplayDeviceInfo.Available()
	kind = AirplayDeviceInfo.Kind()
	network_address = AirplayDeviceInfo.NetworkAddress()
	protected = AirplayDeviceInfo.Protected()
	selected = AirplayDeviceInfo.Selected()
	sound_volume = AirplayDeviceInfo.SoundVolume()
	supports_audio = AirplayDeviceInfo.SupportsAudio()
	supports_video = AirplayDeviceInfo.SupportsVideo()