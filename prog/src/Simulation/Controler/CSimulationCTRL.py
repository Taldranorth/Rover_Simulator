########################################################################
# Fichier qui vient Contenir la Classe Controller de la Simulation
# Initialiser dans Server
########################################################################

#from src.CSimulation.GUI.CSimulationGUI import CSimulationGUI


class CSimulationCTRL:
	def __init__(self, sim_factory, param_factory):
		# On set les factory
		self.sim_factory = sim_factory
		self.param_factory = param_factory

	# Setter
	# Simulation
	def create_simulation(self, CParam):
		# Méthode pour ajouter une simulation par la méthode de la factory
		self.sim_factory.create_simulation(CParam)

	def remove_simulation(self, i):
		# Méthode pour retirer une simulation
		self.sim_factory.remove_simulation(i)

	def get_simulation(self, i):
		# Méthode pour récupérer l'objet SImulation à la I place
		return self.sim_factory.get_simulation(i)


	# Parameter

	def create_parameter(self):
		# Méthode pour ajouter une simulation par la méthode de la factory
		self.param_factory.create_parameter()

	def remove_parameter(self, i):
		# Méthode pour retirer une simulation
		self.param_factory.remove_parameter(i)

	def get_parameter(self, i):
		# Méthode pour récupérer l'objet SImulation à la I place
		return self.param_factory.get_parameter(i)