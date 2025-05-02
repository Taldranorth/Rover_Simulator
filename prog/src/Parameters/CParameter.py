########################################################################
# Fichier qui vient Contenir la Classe Simulation
# Initialiser dans Server
########################################################################

class CParameter:
	def __init__(self):
		# Durée de la Simulation
		self.maxdays = 1

		# Météo
		# Tempête de Sable
		self.sandstorm_probability_spawn = 25
		self.sandstorm_probability_despawn = 25
		self.sandstorm_damage = 5

		# Tempête Solaire
		self.solarstorm_probability_spawn = 25
		self.solarstorm_probability_despawn = 25
		self.solarstorm_damage = 5

		# Température
		self.mintemp = -143
		self.maxtemp = 20

		# Paramètre de Base des Rovers
		self.components = {
			"wheel": {"durability": 100, "resistance": 1, "damage": 1},
			"arm": {"durability": 100, "resistance": 1, "damage": 1},
			"frame": {"durability": 100, "resistance": 1, "damage": 1},
			"camera": {"durability": 100, "resistance": 1, "damage": 1},
			"solar_panel": {"durability": 100, "resistance": 1, "damage": 1},
			"cell": {"durability": 100, "resistance": 1, "damage": 1},
			"antenna": {"durability": 100, "resistance": 1, "damage": 1},
		}
		
		# Paramètre de Base des Rovers
		#Durabilité
		#Roue
		self.wheel_durability = 100
		#Bras
		self.arm_durability = 100
		#Chassis
		self.frame_durability = 100
		#Camera
		self.camera_durability = 100
		#Panneau Solaire
		self.solar_panel_durability = 100
		#Batterie
		self.cell_durability = 100
		#Antenne
		self.antenna_durability = 100

		#Résistance
		#Roue
		self.wheel_rs = 1
		#Bras
		self.arm_rs = 1
		#Chassis
		self.frame_rs = 1
		#Camera
		self.camera_rs = 1
		#Panneau Solaire
		self.solar_panel_rs = 1
		#Batterie
		self.cell_rs = 1
		#Antenne
		self.antenna_rs = 1

		#Dégats par Tour
		#Roue
		self.wheel_damage = 1
		#Bras
		self.arm_damage = 1
		#Chassis
		self.frame_damage = 1
		#Camera
		self.camera_damage = 1
		#Panneau Solaire
		self.solar_panel_damage = 1
		#Batterie
		self.cell_damage = 1
		#Antenne
		self.antenna_damage = 1
		
		
	######### Setter #########

	def set_maxdays(self, change):
		# Méthode pour set la durée de la Simulation
		self.maxdays = change

	# Météo
	# Sandstorm
	def set_sandstorm_probability_spawn(self, change):
		# Méthode pour set la probabilité de spawn d'une tempête de sable
		self.sandstorm_probability_spawn = change

	def set_sandstorm_probability_despawn(self, change):
		# Méthode pour set la probabilité de despawn d'une tempête de sable
		self.sandstorm_probability_despawn = change

	def set_sandstorm_damage(self, change):
		# méthode pour set les dégâts d'une tempête de sable
		self.sandstorm_damage = change

	# SolarSorm
	def set_solarstorm_probability_spawn(self, change):
		# Méthode pour set la probabilité de spawn d'une tempête de sable
		self.solarstorm_probability_spawn = change

	def set_solarstorm_probability_despawn(self, change):
		# Méthode pour set la probabilité de despawn d'une tempête de sable
		self.solarstorm_probability_despawn = change

	def set_solarstorm_damage(self, change):
		# méthode pour set les dégâts d'une tempête de sable
		self.solarstorm_damage = change

	# Température
	def set_maxtemp(self, change):
		# Méthode pour set la température max
		self.maxtemp = change

	def set_mintemp(self, change):
		# Méthode pour set la température min
		self.mintemp = change

	# Composants

	def set_components_durability(self, components, change):
		# Méthode pour set la durabilité d'un composants
		if components == "wheel":
			self.wheel_durability = change
		elif components == "arm":
			self.arm_durability = change
		elif components == "frame":
			self.frame_durability = change
		elif components == "camera":
			self.camera_durability = change
		elif components == "solar_panel":
			self.solar_panel_durability = change
		elif components == "cell":
			self.cell_durability = change
		elif components == "antenna":
			self.antenna_durability = change

	def set_components_resistance(self, components, change):
		# Méthode pour set la résistance d'un composants
		if components == "wheel":
			self.wheel_rs = change
		elif components == "arm":
			self.arm_rs = change
		elif components == "frame":
			self.frame_rs = change
		elif components == "camera":
			self.camera_rs = change
		elif components == "solar_panel":
			self.solar_panel_rs = change
		elif components == "cell":
			self.cell_rs = change
		elif components == "antenna":
			self.antenna_rs = change

	def set_components_damage(self, components, change):
		# Méthode pour set les dégâts du composants pris par tour
		if components == "wheel":
			self.wheel_damage = change
		elif components == "arm":
			self.arm_damage = change
		elif components == "frame":
			self.frame_damage = change
		elif components == "camera":
			self.camera_damage = change
		elif components == "solar_panel":
			self.solar_panel_damage = change
		elif components == "cell":
			self.cell_damage = change
		elif components == "antenna":
			self.antenna_damage = change
	
	### Save / Load ###
		
	def	to_dict(self):
		#Sauvegarde les données dans un dico data
		data = {
			"max_days": self.maxdays,
			"sandstorm": {
				"proba_spawn": self.sandstorm_probability_spawn,
				"proba_despawn": self.sandstorm_probability_despawn,
				"damage": self.sandstorm_damage
			},
			"solarstorm": {
				"proba_spawn": self.solarstorm_probability_spawn,
				"proba_despawn": self.solarstorm_probability_despawn,
				"damage": self.solarstorm_damage
			},
			"temperature": {
				"min": self.mintemp,
				"max": self.maxtemp,
			},
			"components": self.components  
		}
		return data


	def from_dict(self, data):
		#Charge les données depuis le dico data
		self.maxdays = data["maxdays"]
		
		self.sandstorm_probability_spawn = data["sandstorm"]["proba_spawn"]
		self.sandstorm_probability_despawn = data["sandstorm"]["proba_despawn"]
		self.sandstorm_damage = data["sandstorm"]["damage"]
		
		self.solarstorm_probability_spawn = data["solarstorm"]["proba_spawn"]
		self.solarstorm_probability_despawn = data["solarstorm"]["proba_despawn"]
		self.solarstorm_damage = data["solarstorm"]["damage"]
		
		self.mintemp = data["temperature"]["min"]
		self.maxtemp = data["temperature"]["max"]
		
		self.components = data["components"]


