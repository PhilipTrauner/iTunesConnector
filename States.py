class States(object):
	class Playing(object):
		def __get__(self, instance, owner):
			if str(instance.itunes.playerState())[-2:] == "20":
				return True
			return False


	class Paused(object):
		def __get__(self, instance, owner):
			if str(instance.itunes.playerState())[-2:] == "52":
				return True
			return False


	class Stopped(object):
		def __get__(self, instance, owner):
			if str(instance.itunes.playerState())[-2:] == "23":
				return True
			return False


	class FastForward(object):
		def __get__(self, instance, owner):
			if str(instance.itunes.playerState())[-2:] == "10":
				return True
			return False


	class Rewind(object):
		def __get__(self, instance, owner):
			if str(instance.itunes.playerState())[-2:] == "22":
				return True
			return False