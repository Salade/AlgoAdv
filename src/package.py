# -*- coding: UTF-8 -*-

import datetime

import random
import math
from turtle import *


class Point(object):
	
	def __init__(self, x, y):
		self.x = x
		self.y = y	

	def getX(self):
		return self.x

	def getY(self):
		return self.y	

	def afficher(self):
		print "Point de coordonnées : (" + str(self.x) +", " + str(self.y) + ")"

class Arc(object):

	def __init__(self, pointA, pointB):
		self.distance = sqrt( (pointB.getX() - pointA.getX())**2 + (pointB.getY() - pointA.getY())**2 )

	def getDistance(self):
		return self.distance	
	
	def afficher(self):
		print "L'arc est de longueur : " +str(self.distance)


# Class polygone : elle va nous permettre de créer notre polygone
class Polygone(object):

	def __init__(self, nSommets):
		self.nSommets = nSommets

		# Initilisation du polygone, premier point
		pointA = Point(0,0)
		self.mesSommets = [pointA]

		# Le reste des points
		pointB = Point( random.randint(0, 10), random.randint(0, 10) )
		pointB.afficher()
		arcA = Arc(pointA, pointB)
		arcA.afficher()

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
