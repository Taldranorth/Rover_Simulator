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


	###### Dégâts Composants ###### 

	def apply_damage_global(self, lsdamage, temp):
		# Méthode pour appliquer les dégats de manière globale à tout les Composants
		# Roue
		self.wheel1.damage_durability(lsdamage[0], temp)
		self.wheel2.damage_durability(lsdamage[0], temp)
		self.wheel3.damage_durability(lsdamage[0], temp)
		self.wheel4.damage_durability(lsdamage[0], temp)
		#Bras
		self.arm.damage_durability(lsdamage[1], temp)
		#Chassis
		self.frame.damage_durability(lsdamage[2], temp)
		#Camera
		self.camera.damage_durability(lsdamage[3], temp)
		#Panneau Solaire
		self.solar_pannel.damage_durability(lsdamage[4], temp)
		#Batterie
		self.cell.damage_durability(lsdamage[5], temp)
		#Antenne
		self.antenna.damage_durability(lsdamage[6], temp)

	def apply_damage_sandstorm(self, damage, intensity, temp):
		# Méthode pour appliquer les dégats de la tempête de sable
		dmg = damage*intensity
		#Roue
		self.wheel1.damage_durability(dmg, temp)
		self.wheel2.damage_durability(dmg, temp)
		self.wheel3.damage_durability(dmg, temp)
		self.wheel4.damage_durability(dmg, temp)
		#Camera
		self.camera.damage_durability(dmg, temp)
		#Bras
		self.arm.damage_durability(dmg, temp)
		#Panneaux Solaire
		self.solar_pannel.damage_durability(dmg, temp)
		#Chassis
		self.frame.damage_durability(dmg, temp)
		#Antenne
		self.antenna.damage_durability(dmg, temp)

	def apply_damage_solarstorm(self, damage, intensity, temp):
		# Méthode pour appliquer les dégats de la tempête solaire
		dmg = damage*intensity
		#Camera
		self.camera.damage_durability(dmg, temp)
		#Batterie
		self.cell.damage_durability(dmg, temp)
		#Panneau Solaire
		self.solar_pannel.damage_durability(dmg, temp)
		#Antenne
		self.antenna.damage_durability(dmg, temp)
	################################################ 

	# Setter

	def set_durability(self, Components, newdr):
		# Méthode pour set la durabilité d'un composants
		if Components == self.wheel1:
			self.wheel1.set_durability(newdr)
		elif Components == self.wheel2:
			self.wheel2.set_durability(newdr)
		elif Components == self.wheel3:
			self.wheel3.set_durability(newdr)
		elif Components == self.wheel4:
			self.wheel4.set_durability(newdr)
		elif Components == self.arm:
			self.arm.set_durability(newdr)
		elif Components == self.frame:
			self.frame.set_durability(newdr)
		elif Components == self.camera:
			self.camera.set_durability(newdr)
		elif Components == self.solar_pannel:
			self.solar_pannel.set_durability(newdr)
		elif Components == self.cell:
			self.cell.set_durability(newdr)
		elif Components == self.antenna:
			self.antenna.set_durability(newdr)

	def set_resistance(self, Components, newrs):
		# Méthode pour set la résistance d'un composants
		if Components == self.wheel1:
			self.wheel1.set_resistance(newrs)
		elif Components == self.wheel2:
			self.wheel2.set_resistance(newrs)
		elif Components == self.wheel3:
			self.wheel3.set_resistance(newrs)
		elif Components == self.wheel4:
			self.wheel4.set_resistance(newrs)
		elif Components == self.arm:
			self.arm.set_resistance(newrs)
		elif Components == self.frame:
			self.frame.set_resistance(newrs)
		elif Components == self.camera:
			self.camera.set_resistance(newrs)
		elif Components == self.solar_pannel:
			self.solar_pannel.set_resistance(newrs)
		elif Components == self.cell:
			self.cell.set_resistance(newrs)
		elif Components == self.antenna:
			self.antenna.set_resistance(newrs)

	def set_maxtemp(self, Components, newtemp):
		# Méthode pour set la temp min d'un composants
		if Components == self.wheel1:
			self.wheel1.set_maxtemp(newtemp)
		elif Components == self.wheel2:
			self.wheel2.set_maxtemp(newtemp)
		elif Components == self.wheel3:
			self.wheel3.set_maxtemp(newtemp)
		elif Components == self.wheel4:
			self.wheel4.set_maxtemp(newtemp)
		elif Components == self.arm:
			self.arm.set_maxtemp(newtemp)
		elif Components == self.frame:
			self.frame.set_maxtemp(newtemp)
		elif Components == self.camera:
			self.camera.set_maxtemp(newtemp)
		elif Components == self.solar_pannel:
			self.solar_pannel.set_maxtemp(newtemp)
		elif Components == self.cell:
			self.cell.set_maxtemp(newtemp)
		elif Components == self.antenna:
			self.antenna.set_maxtemp(newtemp)
	
	def set_mintemp(self, Components, newtemp):
		# Méthode pour set la temp min d'un composants
		if Components == self.wheel1:
			self.wheel1.set_mintemp(newtemp)
		elif Components == self.wheel2:
			self.wheel2.set_mintemp(newtemp)
		elif Components == self.wheel3:
			self.wheel3.set_mintemp(newtemp)
		elif Components == self.wheel4:
			self.wheel4.set_mintemp(newtemp)
		elif Components == self.arm:
			self.arm.set_mintemp(newtemp)
		elif Components == self.frame:
			self.frame.set_mintemp(newtemp)
		elif Components == self.camera:
			self.camera.set_mintemp(newtemp)
		elif Components == self.solar_pannel:
			self.solar_pannel.set_mintemp(newtemp)
		elif Components == self.cell:
			self.cell.set_mintemp(newtemp)
		elif Components == self.antenna:
			self.antenna.set_mintemp(newtemp)


	def show_status(self):
		status = [
			f"{self.wheel1.name}: Durabilité = {self.wheel1.durability}%, Résistance = {self.wheel1.resistance}",
			f"{self.wheel2.name}: Durabilité = {self.wheel2.durability:.2f}%, Résistance = {self.wheel2.resistance}",
			f"{self.wheel3.name}: Durabilité = {self.wheel3.durability:.2f}%, Résistance = {self.wheel3.resistance}",
			f"{self.wheel4.name}: Durabilité = {self.wheel4.durability:.2f}%, Résistance = {self.wheel4.resistance}",
			f"{self.arm.name}: Durabilité = {self.arm.durability:.2f}%, Résistance = {self.arm.resistance}",
			f"{self.frame.name}: Durabilité = {self.frame.durability:.2f}%, Résistance = {self.frame.resistance}",
			f"{self.camera.name}: Durabilité = {self.camera.durability:.2f}%, Résistance = {self.camera.resistance}",
			f"{self.solar_pannel.name}: Durabilité = {self.solar_pannel.durability:.2f}%, Résistance = {self.solar_pannel.resistance}",
			f"{self.cell.name}: Durabilité = {self.cell.durability:.2f}%, Résistance = {self.cell.resistance}",
			f"{self.antenna.name}: Durabilité = {self.antenna.durability:.2f}%, Résistance = {self.antenna.resistance}",
		]
		return "\n".join(status)


