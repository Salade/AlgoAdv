# -*- coding: UTF-8 -*-

import datetime

# Class polygone : elle va nous permettre de créer notre polygone
class Polygone(object):
	def __init__(self, nSommets):
		self.nSommets = nSommets

	def printNSommets(self):
		print self.nSommets




class Mesurer(object):
	def __init__(self):
		self.tempsDebut = 0
		self.tempsFin = 0
		self.duree = 0
	
	def start(self):
		self.tempsDebut = datetime.datetime.now()

	def end(self):
		self.tempsFin = datetime.datetime.now()
		print ( self.tempsFin - self.tempsDebut )
