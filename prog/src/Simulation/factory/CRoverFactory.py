########################################################################
# Fichier qui vient Contenir la Classe Factory du Rover
########################################################################
from src.Simulation.CRover import CRover

class CRoverFactory:
	def __init__(self):
		self.ls_rover = []

	def create_Rover(self):
		rover = CRover()
		self.ls_rover += [rover]
	