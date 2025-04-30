########################################################################
# Fichier qui vient Contenir les Classes des Controlers Menu
# Initialiser dans Server
########################################################################

from src.Simulation.factory.CSimulationFactory import CSimulationFactory
from src.Parameters.factory.CParameterFactory import CParameterFactory


class CMenuCTRL:
	def __init__(self, menuGUI):

		self.simulation_factory = CSimulationFactory()
		self.parameter_factory = CParameterFactory()
