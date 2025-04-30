########################################################################
# Fichier qui vient Contenir la Classe Factory de la simulation
# Initialiser dans Server
########################################################################

from src.Simulation.CSimulation import CSimulation

class CsimulationFactory:
	def __init__(self):
		self.ls_simulation = []

	def get_simulation(self, i):
		# Méthode pour retourner l'objet simulation
		return self.ls_simulation[i]

	def create_simulation(self, CParam):
		# Méthode pour ajouter une simulation
		simulation = Csimulation(CPram)
		self.ls_simulation += [simulation]

	def remove_simulation(self, i):
		# Méthode pour retirer une simulation
		self.ls_simulation = self.ls_simulation[:i] + self.ls_simulation[i+1:]