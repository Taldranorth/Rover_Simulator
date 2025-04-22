########################################################################
# Fichier qui vient Contenir la Classe du Rover
########################################################################

from src.Simulation.CComponents import CComponents


class CRover:
	def __init__(self):
		# Initialisation des Attributs
		# liste des Composante
		# Roue
		self.wheel1 = CComponents("Roue1", 25)
		self.wheel2 = CComponents("Roue2", 25)
		self.wheel3 = CComponents("Roue3", 25)
		self.wheel4 = CComponents("Roue4", 25)		
		# Bras
		self.arm = CComponents("Bras", 25)
		# Chassis
		self.frame = CComponents("Chassis", 25)
		# Caméra
		self.camera = CComponents("Camera", 25)
		# Panneau Solaire
		self.solar_pannel = CComponents("Panneaux Solaire", 25)
		# Batterie
		self.cell = CComponents("Batterie", 25)
		# Antenne
		self.antenna = CComponents("Antenne", 25)

	def apply_damage_global(self, damage):
		# Méthode pour appliquer les dégats de manière globale à tout les Composants
		# Roue
		self.wheel1.damage_durability(damage)
		self.wheel2.damage_durability(damage)
		self.wheel3.damage_durability(damage)
		self.wheel4.damage_durability(damage)
		#Bras
		self.arm.damage_durability(damage)
		#Chassis
		self.frame.damage_durability(damage)
		#Camera
		self.camera.damage_durability(damage)
		#Panneau Solaire
		self.solar_pannel.damage_durability(damage)
		#Batterie
		self.cell.damage_durability(damage)
		#Antenne
		self.antenna.damage_durability(damage)

	def apply_damage_sandstorm(self, damage, intensity):
		# Méthode pour appliquer les dégats de la tempête de sable
		dmg = damage*intensity
		#Roue
		self.wheel1.damage_durability(dmg)
		self.wheel2.damage_durability(dmg)
		self.wheel3.damage_durability(dmg)
		self.wheel4.damage_durability(dmg)
		#Camera
		self.camera.damage_durability(dmg)
		#Bras
		self.arm.damage_durability(dmg)
		#Panneaux Solaire
		self.solar_pannel.damage_durability(dmg)
		#Chassis
		self.frame.damage_durability(dmg)
		#Antenne
		self.antenna.damage_durability(dmg)

	def apply_damage_solarstorm(self, damage, intensity):
		# Méthode pour appliquer les dégats de la tempête solaire
		dmg = damage*intensity
		#Camera
		self.camera.damage_durability(dmg)
		#Batterie
		self.cell.damage_durability(dmg)
		#Panneau Solaire
		self.solar_pannel.damage_durability(dmg)
		#Antenne
		self.antenna.damage_durability(dmg)


	def change_durability(self, Components, newdr):
		# Méthode pour changer la durabilité d'un composants
		if Components == self.wheel1:
			self.wheel1.change_durability(newdr)
		elif Components == self.wheel2:
			self.wheel2.change_durability(newdr)
		elif Components == self.wheel3:
			self.wheel3.change_durability(newdr)
		elif Components == self.wheel4:
			self.wheel4.change_durability(newdr)
		elif Components == self.arm:
			self.arm.change_durability(newdr)
		elif Components == self.frame:
			self.frame.change_durability(newdr)
		elif Components == self.camera:
			self.camera.change_durability(newdr)
		elif Components == self.solar_pannel:
			self.solar_pannel.change_durability(newdr)
		elif Components == self.cell:
			self.cell.change_durability(newdr)
		elif Components == self.antenna:
			self.antenna.change_durability(newdr)

	def change_resistance(self, Components, newrs):
		# Méthoder pour changer la résistance d'un composants
		if Components == self.wheel1:
			self.wheel1.change_resistance(newrs)
		elif Components == self.wheel2:
			self.wheel2.change_resistance(newrs)
		elif Components == self.wheel3:
			self.wheel3.change_resistance(newrs)
		elif Components == self.wheel4:
			self.wheel4.change_resistance(newrs)
		elif Components == self.arm:
			self.arm.change_resistance(newrs)
		elif Components == self.frame:
			self.frame.change_resistance(newrs)
		elif Components == self.camera:
			self.camera.change_resistance(newrs)
		elif Components == self.solar_pannel:
			self.solar_pannel.change_resistance(newrs)
		elif Components == self.cell:
			self.cell.change_resistance(newrs)
		elif Components == self.antenna:
			self.antenna.change_resistance(newrs)



