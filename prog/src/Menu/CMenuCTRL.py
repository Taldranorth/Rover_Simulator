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
