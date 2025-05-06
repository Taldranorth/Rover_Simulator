##############################
# Fichier test qui contient les fonctions pour dessiner avec matplotlib
##############################

import os
import sys

from PyQt6 import QtCore, QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure


# Liste des Graphes Possibles:
# - Évolution de la Météo
# - Évolution de la température
# - Évolution de l'état des Composants
# - Évolution du nombre de Rover en état de marche
# Cela définit donc 4 type:
# - meteo
# - temperature
# - components
# - rover



class CGraph(FigureCanvas):
	def __init__(self, type, parent=None, width=5, height=4, dpi=100):
		# Ont définit la taille
		fig = Figure(figsize=(width, height), dpi=dpi)
		super().__init__(fig)

		self.type = type
		# On met en places les axes
		self.axes = fig.add_subplot(111)

		if type == "components":
			self.ydata = [[],[],[],[],[],[],[]]
			self.xdata = []
		elif type == "meteo":
			self.ydata = [[],[],[]]
			self.xdata = []
		else:
			self.xdata = []
			self.ydata = []

	def load_graph(self, xdata, ydata):
		# Méthode pour load les données d'un graph
		# On charge les données
		self.xdata = xdata
		self.ydata = ydata
		print("type:", self.type)
		print("xdata:",xdata)
		print("ydata:",ydata)
		# On change le graph
		# On clear
		self.axes.cla()
		# On affiche
		if self.type == "components":
			print("components")
			print("time:",len(self.xdata))
			print("components[0]:",len(self.ydata[0]))
			i = 0
			for string in ["wheel","arm","frame","camera","solar_panel","cell","antenna"]:
				print(self.ydata[i])
				self.axes.plot(self.xdata,self.ydata[i], label = string)
				i += 1
			self.axes.legend()
		elif self.type == "meteo":
			print("meteo")
			self.axes.plot(self.xdata, self.ydata[0], label = "SandStorm")
			self.axes.plot(self.xdata, self.ydata[1], label = "SolarStorm")
			self.axes.plot(self.xdata, self.ydata[2], label = "Clear")
			self.axes.legend()
		elif self.type == "temperature":
			print("temperature")
			self.axes.plot(self.xdata, self.ydata)
		elif self.type == "rover":
			print("rover")
			self.axes.plot(self.xdata, self.ydata, label = "Rover Alive")
			self.axes.legen()

	def update_components(self, lx, time):
		# Méthode pour Update le graph
		# On récup les données
		for i in range(len(lx)):
			self.ydata[i] += [lx[i]]
		self.xdata += [time]
		# On clear
		self.axes.cla()
		# On affiche
		i = 0
		for string in ["wheel","arm","frame","camera","solar_panel","cell","antenna"]:
			self.axes.plot(self.xdata,self.ydata[i], label = string)
			i += 1
		self.axes.legend()

	def update_meteo(self, time, meteo):
		# Méthode pour Update le graph meteo
		print("On update le graph meteo")
		print(time)
		print(meteo)
		if meteo == "SandStorm":
			self.ydata[0] += [1]
			self.ydata[1] += [0]
			self.ydata[2] += [0]
		elif meteo == "SolarStorm":
			self.ydata[0] += [0]
			self.ydata[1] += [1]
			self.ydata[2] += [0]
		elif meteo == "Clear":
			self.ydata[0] += [0]
			self.ydata[1] += [0]
			self.ydata[2] += [1]
		#print("time:",self.ydata)
		self.xdata += [time]
		print("time: ",self.xdata)
		print("meteo: ",self.ydata)
		# On Clear
		self.axes.cla()
		# On affiche
		self.axes.plot(self.xdata, self.ydata[0], label = "SandStorm")
		self.axes.plot(self.xdata, self.ydata[1], label = "SolarStorm")
		self.axes.plot(self.xdata, self.ydata[2], label = "Clear")
		self.axes.legend()

	def update_temp(self, time, temp):
		# Méthode pour update le graph temperature
		print("On update le graph température")
		print(time)
		print(temp)
		# On ajoute au données
		self.xdata += [time]
		self.ydata += [temp]
		print("time: ",self.xdata)
		print("temp: ", self.ydata)
		# On clear
		self.axes.cla()
		# On draw
		self.axes.plot(self.xdata, self.ydata)

	def update_rover(self, time, nbrover):
		# Méthode pour udpate le graph rover
		print("On update le graph rover")
		print(time)
		print(nbrover)
		# On ajoute au données
		self.xdata += [time]
		self.ydata += [nbrover]
		print("time: ",self.xdata)
		print("rover: ", self.ydata)
		# On clear
		self.axes.cla()
		# On draw
		self.axes.plot(self.xdata, self.ydata, label = "Rover Alive")
		self.axes.legend()