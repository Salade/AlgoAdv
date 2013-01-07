#!/usr/bin/python
# -*- coding: UTF-8 -*-

import package

class main:

	# Simple instanciation d'une classe Polygone définie dans "package"
	a = package.Polygone(10)
	maMesure= package.Mesurer()
	
	maMesure.start()
	a.printNSommets()
	maMesure.end()
