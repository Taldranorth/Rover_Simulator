########################################################################
# Fichier qui vient Contenir la Classe du Rover
########################################################################

from src.Simulation.CComponents import CComponents


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

	def apply_damage_global(self, damage):
		# Méthode pour appliquer les dégats de manière globale
		wheel1.damage_durability()
		wheel2.damage_durability()
		wheel3.damage_durability()
		wheel4.damage_durability()

	def apply_damage_sandstorm(self, damage, intensity):
		# Méthode pour appliquer les dégats de la tempête de sable
		pass

	def apply_damage_solarstorm(self, damage, intensity):
		# Méthode pour appliquer les dégats de la tempête solaire
		pass


	def change_durability(self, Components, newdr):
		# Méthode pour changer la durabilité d'un composants
		if Components == wheel1:
			wheel1.change_durability(newdr)
		elif Components == wheel2:
			wheel2.change_durability(newdr)
		elif Components == wheel3:
			wheel3.change_durability(newdr)
		elif Components == wheel4:
			wheel4.change_durability(newdr)
		elif Components == arm:
			arm.change_durability(newdr)
		elif Components == frame:
			frame.change_durability(newdr)
		elif Components == camera:
			camera.change_durability(newdr)
		elif Components == solar_pannel:
			solar_pannel.change_durability(newdr)
		elif Components == cell:
			cell.change_durability(newdr)
		elif Components == antenna:
			antenna.change_durability(newdr)

	def change_resistance(self, Components, newrs):
		# Méthoder pour changer la résistance d'un composants
		if Components == wheel1:
			wheel1.change_resistance(newrs)
		elif Components == wheel2:
			wheel2.change_resistance(newrs)
		elif Components == wheel3:
			wheel3.change_resistance(newrs)
		elif Components == wheel4:
			wheel4.change_resistance(newrs)
		elif Components == arm:
			arm.change_resistance(newrs)
		elif Components == frame:
			frame.change_resistance(newrs)
		elif Components == camera:
			camera.change_resistance(newrs)
		elif Components == solar_pannel:
			solar_pannel.change_resistance(newrs)
		elif Components == cell:
			cell.change_resistance(newrs)
		elif Components == antenna:
			antenna.change_resistance(newrs)



