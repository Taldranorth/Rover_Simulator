########################################################################
# Fichier qui vient Contenir les Classes des Controlers Menu
# Initialiser dans Server
########################################################################

from src.Simulation.factory.CSimulationFactory import CSimulationFactory
from src.Parameters.factory.CParameterFactory import CParameterFactory


class CMenuCTRL:
	def __init__(self, sim_factory, param_factory):

		self.simulation_factory = sim_factory
		self.parameter_factory = param_factory
