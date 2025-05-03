########################################################################
# Fichier qui vient Contenir la Classe du Rover
# Initialiser dans Server
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

		self.dead = False

		#Historique états des composants des rovers
		self.history = {name: [] for name in self.components.keys()}


	###### Dégâts Composants ###### 

	def apply_damage_global(self, lsdamage, temp):
		# Méthode pour appliquer les dégats de manière globale à tout les Composants
		# Roue
		if self.wheel1.durability > 0:
			self.wheel1.damage_durability(lsdamage[0], temp)
		if self.wheel2.durability > 0:
			self.wheel2.damage_durability(lsdamage[0], temp)
		if self.wheel3.durability > 0:
			self.wheel3.damage_durability(lsdamage[0], temp)
		if self.wheel4.durability > 0:
			self.wheel4.damage_durability(lsdamage[0], temp)
		#Bras
		if self.arm.durability > 0:
			self.arm.damage_durability(lsdamage[1], temp)
		#Chassis
		if self.frame.durability > 0:
			self.frame.damage_durability(lsdamage[2], temp)
		#Camera
		if self.camera.durability > 0:
			self.camera.damage_durability(lsdamage[3], temp)
		#Panneau Solaire
		if self.solar_pannel.durability > 0:
			self.solar_pannel.damage_durability(lsdamage[4], temp)
		#Batterie
		if self.cell.durability > 0:
			self.cell.damage_durability(lsdamage[5], temp)
		#Antenne
		if self.antenna.durability > 0:
			self.antenna.damage_durability(lsdamage[6], temp)

		for name, comp in self.components.items():
			self.history[name].append(comp.durability)

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
		
		for name, comp in self.components.items():
			self.history[name].append(comp.durability)

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
		
		for name, comp in self.components.items():
			self.history[name].append(comp.durability)
	################################################ 

	# Setter

	def set_durability(self, Components, newdr):
		# Méthode pour set la durabilité d'un composants
		if Components == "wheel1":
			self.wheel1.set_durability(newdr)
		elif Components == "wheel2":
			self.wheel2.set_durability(newdr)
		elif Components == "wheel3":
			self.wheel3.set_durability(newdr)
		elif Components == "wheel4":
			self.wheel4.set_durability(newdr)
		elif Components == "arm":
			self.arm.set_durability(newdr)
		elif Components == "frame":
			self.frame.set_durability(newdr)
		elif Components == "camera":
			self.camera.set_durability(newdr)
		elif Components == "solar_pannel":
			self.solar_pannel.set_durability(newdr)
		elif Components == "cell":
			self.cell.set_durability(newdr)
		elif Components == "antenna":
			self.antenna.set_durability(newdr)

	def set_resistance(self, Components, newrs):
		# Méthode pour set la résistance d'un composants
		if Components == "wheel1":
			self.wheel1.set_resistance(newrs)
		elif Components == "wheel2":
			self.wheel2.set_resistance(newrs)
		elif Components == "wheel3":
			self.wheel3.set_resistance(newrs)
		elif Components == "wheel4":
			self.wheel4.set_resistance(newrs)
		elif Components == "arm":
			self.arm.set_resistance(newrs)
		elif Components == "frame":
			self.frame.set_resistance(newrs)
		elif Components == "camera":
			self.camera.set_resistance(newrs)
		elif Components == "solar_pannel":
			self.solar_pannel.set_resistance(newrs)
		elif Components == "cell":
			self.cell.set_resistance(newrs)
		elif Components == "antenna":
			self.antenna.set_resistance(newrs)

	def set_maxtemp(self, Components, newtemp):
		# Méthode pour set la temp min d'un composants
		if Components == "wheel1":
			self.wheel1.set_maxtemp(newtemp)
		elif Components == "wheel2":
			self.wheel2.set_maxtemp(newtemp)
		elif Components == "wheel3":
			self.wheel3.set_maxtemp(newtemp)
		elif Components == "wheel4":
			self.wheel4.set_maxtemp(newtemp)
		elif Components == "arm":
			self.arm.set_maxtemp(newtemp)
		elif Components == "frame":
			self.frame.set_maxtemp(newtemp)
		elif Components == "camera":
			self.camera.set_maxtemp(newtemp)
		elif Components == "solar_pannel":
			self.solar_pannel.set_maxtemp(newtemp)
		elif Components == "cell":
			self.cell.set_maxtemp(newtemp)
		elif Components == "antenna":
			self.antenna.set_maxtemp(newtemp)
	
	def set_mintemp(self, Components, newtemp):
		# Méthode pour set la temp min d'un composants
		if Components == "wheel1":
			self.wheel1.set_mintemp(newtemp)
		elif Components == "wheel2":
			self.wheel2.set_mintemp(newtemp)
		elif Components == "wheel3":
			self.wheel3.set_mintemp(newtemp)
		elif Components == "wheel4":
			self.wheel4.set_mintemp(newtemp)
		elif Components == "arm":
			self.arm.set_mintemp(newtemp)
		elif Components == "frame":
			self.frame.set_mintemp(newtemp)
		elif Components == "camera":
			self.camera.set_mintemp(newtemp)
		elif Components == "solar_pannel":
			self.solar_pannel.set_mintemp(newtemp)
		elif Components == "cell":
			self.cell.set_mintemp(newtemp)
		elif Components == "antenna":
			self.antenna.set_mintemp(newtemp)

	def is_dead(self):
		# Méthode pour vérifier si le Rover Tourne encore
		if self.wheel1.durability > 0:
			return False
		if self.wheel2.durability > 0:
			return False
		if self.wheel3.durability > 0:
			return False
		if self.wheel4.durability > 0:
			return False
		if self.arm.durability > 0:
			return False
		if self.frame.durability > 0:
			return False
		if self.camera.durability > 0:
			return False
		if self.solar_pannel.durability > 0:
			return False
		if self.cell.durability > 0:
			return False
		if self.antenna.durability > 0:
			return False

		self.dead = True
		return True


	def get_components_durability(self, Components):
		if Components == "wheel1":
			return self.wheel1.durability
		elif Components == "wheel2":
			return self.wheel2.durability
		elif Components == "wheel3":
			return self.wheel3.durability
		elif Components == "wheel4":
			return self.wheel4.durability
		elif Components == "arm":
			return self.arm.durability
		elif Components == "frame":
			return self.frame.durability
		elif Components == "camera":
			return self.camera.durability
		elif Components == "solar_pannel":
			return self.solar_pannel.durability
		elif Components == "cell":
			return self.cell.durability
		elif Components == "antenna":
			return self.antenna.durability

	def get_components_durability_all(self):
		ls = []
		for string in ["wheel1","arm","frame","camera","solar_pannel","cell","antenna"]:
			ls += [self.get_components_durability(string)]
		return ls


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


		#### Save/Load ####
	def to_dict(self):
		# Méthode pour Sauvegarder dans un dico
		data = {
			"dead": self.dead,
			"components": {
				"wheel1": self.wheel1.to_dict(),
				"wheel2": self.wheel2.to_dict(),
				"wheel3": self.wheel3.to_dict(),
				"wheel4": self.wheel4.to_dict(),
				"arm": self.arm.to_dict(),
				"frame": self.frame.to_dict(),
				"camera": self.camera.to_dict(),
				"solar_pannel": self.solar_pannel.to_dict(),
				"cell": self.cell.to_dict(),
				"antenna": self.antenna.to_dict()			
			},
			"history": self.history
		}
		return data


	def from_dict(self, data):
		# Méthode pour Charger depuis un dico
		self.dead = data["dead"]
		
		self.wheel1.from_dict(data["components"]["wheel1"])
		self.wheel2.from_dict(data["components"]["wheel2"])
		self.wheel3.from_dict(data["components"]["wheel3"])
		self.wheel4.from_dict(data["components"]["wheel4"])
		
		self.arm.from_dict(data["components"]["arm"])
		self.frame.from_dict(data["components"]["frame"])
		self.camera.from_dict(data["components"]["camera"])
		self.solar_pannel.from_dict(data["components"]["solar_pannel"])
		self.cell.from_dict(data["components"]["cell"])
		self.antenna.from_dict(data["components"]["antenna"])
		
		
