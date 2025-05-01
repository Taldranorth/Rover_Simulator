########################################################################
# Fichier qui vient Contenir les Classes des Controlers Menu
# Initialiser dans User
########################################################################

from src.Simulation.factory.CSimulationFactory import CSimulationFactory
from src.Parameters.factory.CParameterFactory import CParameterFactory


class CMenuCTRL:
	def __init__(self, main_window, sim_factory, param_factory):
		# link vers la window
		self.main_window = main_window
		# link vers les factory
		self.simulation_factory = sim_factory
		self.parameter_factory = param_factory




	#### Button ####

	def new_simulation(self):
		# Méthode pour gérer la création d'une simulation
		self.main_window.change_GUI("CParameterGUI")

	def load_simulation(self, filename):
		# Méthode pour gérer le chargement d'une simulation


		pass

	def manage_result(self):
		# Méthode pour gérer les résultat enregistrés
		pass


	def exit(self):
		# Méthode exit
		self.main_window.exit()
