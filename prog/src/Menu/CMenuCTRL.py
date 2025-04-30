########################################################################
# Fichier qui vient Contenir la Classe du Controler Menu
# Initialiser dans Server
########################################################################

from src.Menu.CMenuGUI import CMenuGUI
from src.Simulation.factory.CSimulationFactory import CSimulationFactory
from src.Parameters.factory.CParameterFactory import CParameterFactory


class CMenuCTRL:
	def __init__(self, menuGUI):

		self.GUI = menuGUI
		self.simulation_factory = CSimulationFactory()
		self.parameter_factory = CParameterFactory()
		pass
