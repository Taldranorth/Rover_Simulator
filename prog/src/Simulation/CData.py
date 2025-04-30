########################################################################
# Fichier qui vient Contenir la Classe des données
# Initialiser dans Server
########################################################################

from src.Simulation.CRover import CRover
from src.Simulation.Factory.CRoverFactory import CRoverFactory

# Les diférents fichiers sont sauvegardés sous:
# - project/data/save/results -> résultats de simulation
# - project/data/save/parameters -> fichiers sauvegardes des paramètres
# - project/data/save/simulation -> fichiers sauvegardes des simulation
# l'extension préféré et le .sav


class CData:
	def __init__(self):
		pass

	def load_parameter(self, filename):
		# Méthode pour charger les Paramètre depuis un fichier filename
		pass

	def save_parameter(self, filename):
		# Méthode pour sauvegarder les Paramètre dans un fichier filename
		pass

	def load_simulation(self, filename):
		# Méthode pour charger une Simulation depuis un fichier filename
		pass

	def save_simulation(self, filename):
		# Méthode pour sauvegarder une Simulation dans un fichier filename
		pass