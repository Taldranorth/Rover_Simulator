import sys
import random
from PyQt5.QtWidgets import *
#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas	#intègre matplotlib dans pyqt
#from matplotlib.figure import Figure
import pyqtgraph as pgraph

# https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/

#from PyQt6 import QtWidgets
#import pyqtgraph as pgraph



class RoverGraph(QWidget):
	def __init__(self):
		super().__init__()		#Init classe widjet
		self.setWindowTitle("Mars Rover Simulation")
		self.setGeometry(100, 100, 800, 500)	#Position et taille (x, y, largeur, hauteur)
		
		layout1 = QVBoxLayout()	#Layout pour organiser les fenêtres
		self.setLayout(layout1)	#L'ajoute à la fenêtre
		
		#Config titre du layout
		title = QLabel("Rover Graphic Interface")
		title.setStyleSheet("font-size: 20px; font-weight: bold;")
		layout1.addWidget(title)
		
		#Création des graphes
		self.graph1 = self.create_graph("Graphic 1", "X", "Y")
		layout1.addWidget(self.graph1)  	#Ajout du graphique dans l'interface
		
		self.graph2 = self.create_graph("Graphic 2", "X", "Y")
		layout1.addWidget(self.graph2)  	#Ajout du graphique dans l'interface

		#tracer les données ici ( voir pour en faire une méthode de récup de données)
	
	#Fonction qui crée un widget graphique (pour l'instant vide)
	def create_graph(self, title, xlabel, ylabel):
		plot_widget = pgraph.PlotWidget()
		#Titre + noms axes
		plot_widget.setTitle(title)  
		plot_widget.setLabel("left", ylabel)       
		plot_widget.setLabel("bottom", xlabel)      
		plot_widget.showGrid(x=True, y=True)     #Affichage de la grille (au choix oui ou non)
		#Limites des axes
		plot_widget.setXRange(0, 10)             
		plot_widget.setYRange(0, 10) 
		return plot_widget           


if __name__ == "__main__":
	app = QApplication(sys.argv)	#Création de l'appli pyqt
	window = RoverGraph()
	window.show()	#Affiche la fenetre (obligé car caché à l'init)
	sys.exit(app.exec_())	#Start la boucle et continue jusque la fermeture de la fenetre

