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


class Info(object):
	class Name(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().name()


	class Artist(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().artist()


	class Album(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().album()


	class Rating(object):
		def __get__(self, instance, owner):
			return instance.itunes.current_track().rating()


class Player(object):
	def __init__(self, itunes):
		self.itunes = itunes


	def next(self):
		self.itunes.next_track()


	def back(self):
		self.itunes.back_track()


	playing = States.Playing()
	paused = States.Paused()
	stopped = States.Stopped()


class Track(object):
	def __init__(self, itunes):
		self.itunes = itunes


	name = Info.Name()
	artist = Info.Artist()
	album = Info.Album()
	rating = Info.Rating()


class iTunes(object):
	itunes = app("iTunes")
	player = Player(itunes)
	track = Track(itunes)