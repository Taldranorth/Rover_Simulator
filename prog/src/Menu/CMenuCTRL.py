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
		# Méthode pour gérer le chargement d'une simulation avec le filename donné
		# On Créer une Instace de Paramètre
		self.parameter_factory.create_parameter()
		# On Créer une Instance de Simulation
		self.simulation_factory.create_simulation(self.parameter_factory.get_parameter(0))
		# On Charge la save
		self.simulation_factory.load_simulation(0, filename)
		# Charge le GUI simulation
		self.main_window.change_GUI("CSimulationGUI")
		# On Update l'interface
		self.main_window.widget.update_load()

	def manage_result(self):
		# Méthode pour gérer les résultat enregistrés
		pass


	def exit(self):
		# Méthode exit
		self.main_window.exit()
