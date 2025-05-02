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



class MplCanvas(FigureCanvas):

	def __init__(self, type, parent=None, width=5, height=4, dpi=100):
		# Ont définit la taille
		fig = Figure(figsize=(width, height), dpi=dpi)
		super().__init__(fig)

		self.type = type
		# On met en places les axes
		self.axes = fig.add_subplot(111)

		self.xdata = []
		self.ydata = []


	#def update(self, x, y):
		# Méthode pour Update le graph
	#	self.axes.plot(x,y)

	def update_meteo(self, time, meteo):
		# Méthode pour Update le graph meteo
		print("On update le graph meteo")
		print(time)
		print(meteo)
		pass

	def update_temp(self, time, temp):
		# Méthode pour update le graph temperature
		print("On update le graph température")
		print(time)
		print(temp)
		# On ajoute au données
		self.xdata += [time]
		self.ydata += [temp]
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
		# On clear
		self.axes.cla()
		# On draw
		self.axes.plot(self.xdata, self.ydata)

def graph_components_stat(type):
	# Fonction pour créer un graph matplotlib sur l'évolution des composants
	# Créer le matplotlib figure
	# which defines a single set of axes as self.axes.
	graph = MplCanvas(type)
	#if type == "components":
	#	graph.axes.plot([0,1,2,3,4], [10,1,20,3,40])


	return graph