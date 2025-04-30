########################################################################
# Fichier qui vient Contenir la Classe Factory de la simulation
# Initialiser dans Server
########################################################################

from src.Simulation.CSimulation import CSimulation

class CSimulationFactory:
	def __init__(self):
		self.ls_simulation = []
		self.nb = 0

	def get_simulation(self, i):
		# Méthode pour retourner l'objet simulation
		return self.ls_simulation[i]

	def create_simulation(self, CParam):
		# Méthode pour ajouter une simulation
		simulation = CSimulation(CParam)
		self.ls_simulation += [simulation]
		self.nb += 1

	def remove_simulation(self, i):
		# Méthode pour retirer une simulation
		self.ls_simulation = self.ls_simulation[:i] + self.ls_simulation[i+1:]


	def create_Rover(self, i):
		# Méthode pour la création d'un Rover
		print("Créer Rover dans la Simulation N°",i)
		self.ls_simulation[i].create_Rover()