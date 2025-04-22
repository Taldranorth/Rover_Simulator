########################################################################
# Fichier qui vient Contenir la Classe Simulation
########################################################################

class CParameter:
	def __init__(self):
		# Durée de la Simulation
		self.maxdays = 0

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
		
        




