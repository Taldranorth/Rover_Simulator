########################################################################
# Fichier qui vient Contenir la Classe Factory du Rover
########################################################################
from src.Simulation.CRover import CRover

class CRoverFactory:
	def __init__(self):
		ls_rover = []
		pass

	def create_Rover(self):
		rover = CRover()
		ls_rover += [rover]
	