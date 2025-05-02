########################################################################
# Fichier qui vient Contenir la Classe Factory de la simulation
# Initialiser dans Server
########################################################################

from src.Simulation.CSimulation import CSimulation
from src.Simulation.CData import CData

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
		self.nb -= 1


	def create_Rover(self, i):
		# Méthode pour la création d'un Rover
		print("Créer Rover dans la Simulation N°",i)
		self.ls_simulation[i].create_Rover()

	#### Getter ####

	def get_meteo(self, i):
		# Méthode pour récup la météo de la Iieme Simulation
		return self.ls_simulation[i].get_meteo()

	def get_day(self, i):
		# Méthode pour récup le jour de la Iième Simulation
		return self.ls_simulation[i].get_day()

	def get_hour(self, i):
		return self.ls_simulation[i].get_hour()

	def get_nbrover(self, i):
		return self.ls_simulation[i].get_nbrover()

	def get_temp(self,i):
		return self.ls_simulation[i].get_temp()

	def get_alive_rover(self, i):
		return self.ls_simulation[i].get_alive_rover()


	def get_components_durability_all(self, isim, irover):
		return self.ls_simulation[isim].get_components_durability_all(irover)

	#### Save/Load ####
	def save_simulation(self, i, filename):
		# Méthode pour gérer la sauvegarde d'une simulation
		# On récup les data
		data = self.ls_simulation[i].to_dict()
		# On sauvegarde
		cdata = CData()
		cdata.save_simulation(data, filename)


	def load_simulation(self, i, filename):
		# Méthode pour gérer le chargement d'une simulation
		# On récup les données
		cdata = CData()
		data = cdata.load_simulation(filename)
		if data:
			# On les charges
			self.ls_simulation[i].from_dict(data)

