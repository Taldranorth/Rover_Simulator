########################################################################
# Fichier qui vient Contenir la Classe du Rover
########################################################################

from "./usr/Simulation/CComponents.py" import CComponents


class CRover:
	def __init__(self):
		# Initialisation des Attributs
		# liste des Composante
		# Roue
		wheel1 = CComponents("Roue1", 25)
		wheel2 = CComponents("Roue2", 25)
		wheel3 = CComponents("Roue3", 25)
		wheel4 = CComponents("Roue4", 25)		
		# Bras
		arm = CComponents("Bras", 25)
		# Chassis
		frame = CComponents("Chassis", 25)
		# Caméra
		camera = CComponents("Camera", 25)
		# Panneau Solaire
		solar_pannel = CComponents("Panneaux Solaire", 25)
		# Batterie
		cell = CComponents("Batterie", 25)
		# Antenne
		antenna = CComponents("Antenne", 25)




		pass
