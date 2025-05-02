########################################################################
# Fichier qui vient Contenir la Classe des données
# Initialiser dans Server
########################################################################

import sys
import os
import json

from src.Simulation.CRover import CRover
from src.Simulation.factory.CRoverFactory import CRoverFactory


# Les diférents fichiers sont sauvegardés sous:
# - project/data/save/results -> résultats de simulation
# - project/data/save/parameters -> fichiers sauvegardes des paramètres
# - project/data/save/simulation -> fichiers sauvegardes des simulation
# l'extension préféré et le .sav


def scan_directory(directory):
	# Fonctions qui retourne la liste des fichiers stockés dans le répertoire
	if not os.path.exists(directory):
		print("Aucun fichier dans ce répertoire")
		return []
	print(directory)
	return os.listdir(directory)

def scan_parameter_file():
	# Fonction pour liste les fichiers stockés dans le répertoire des paramètres
	# Normalement on est dans prog
	current_directory = os.getcwd()
	# On se place dans data/save/parameters
	current_directory += "/data/save/parameters"
	result = scan_directory(current_directory)

	return result

def scan_result_file():
	# Fonction pour liste les fichiers stockés dans le répertoire des résultats
	# Normalement on est dans prog
	current_directory = os.getcwd()
	# On se place dans data/save/results
	current_directory += "/data/save/results"
	result = scan_directory(current_directory)

	return result

def scan_simulation_file():
	# Fonction pour liste les fichiers stockés dans le répertoire des simulations
	# Normalement on est dans prog
	current_directory = os.getcwd()
	# On se place dans data/save/simulation
	current_directory += "/data/save/simulation"
	result = scan_directory(current_directory)

	return result



"""
data = {
	...
	...
}
CData().save_simulation(data, filename) filename non obligaotire car par crée si inexistant

Choses a sauvegarde durant la simu:
	- le jour
	- l'heure
	- la température actuelle
	- tempetes (présence et intensité)
	- état des rovers et leur nombre
	- graphe des courbes d évolution
"""

"""
Pour les preset save:
	- la durée de la simulation
	- la proba d'apparition des tempetes (sable et solaire)
	- la proba de dispawn des ces tempetes et les degats créés
	- durabilité, résistance, dégats de chaque composant des rovers

"""


class CData:
	def __init__(self, base_dir="data/save/"):
		self.base_dir = os.getcwd()+"/"+base_dir
		self.paths = {
			"parameters": os.path.join(self.base_dir, "parameters"),
			"simulation": os.path.join(self.base_dir, "simulation"),
			"results": os.path.join(self.base_dir, "results")
			}
		#Création des répertoire s'ils n'existent pas
		for path in self.paths.values():
			os.makedirs(path, exist_ok = True)
			
	def get_path(self, category, filename):
		#Méthode qui construit le chemin du fichier en s'assurant de son extension
		#Vérifie que la catégorie existe
		if category not in self.paths:
			raise ValueError(f"Catégorie de sauvegarde inconnue: {category}")
		#Si le nom n'as pas l'extesion on la rajoute
		if not filename.endswith(".sav"):
			filename += ".sav"
		print(self.paths[category])
		print(filename)
		return os.path.join(self.paths[category], filename)

	def save(self,category, data, filename=None):
		#Méthode qui sauvergarde les données en paramètre dans la catégorie spécifiée avec son nom de fichier custom (ou prédefini)
		#Si le nom de fichier n'est pas précisé on en crée un
		if filename is None:
			filename = f"{category}_Année_Mois_Jour"  #Voir pour inégrer le format classique d'un nom de save
		path = self.get_path(category, filename)
		with open(path, 'w+') as f:
			json.dump(data, f, indent=4)
		print("Sauvegarde effectué")
		
	def load(self, category, filename):
		#Méthode qui charge les données depuis le fichier de la catégorie spécifié
		path = self.get_path(category, filename)
		#Si le chemin n'existe pas on retourne une erreur
		if not os.path.exists(path):
			print("Fichier introuvable")
			return {}
		with open(path, 'r') as f:
			return json.load(f)
		print("Chargement des données réussi")	
	
	def save_parameters(self,data, filename="default"):
		self.save("parameters", data, filename)
		
	def load_parameters(self, filename="default"):
		return self.load("parameters", filename)

	def save_simulation(self,data, filename=None):
		self.save("simulation", data, filename)
		
	def load_simulation(self, filename):
		return self.load("simulation", filename)
			
	def save_results(self,data, filename=None):
		self.save("results", data, filename)
		
	def load_results(self, filename):
		return self.load("results", filename)

