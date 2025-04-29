########################################################################
# Fichier qui vient Contenir la Classe de la Simulation
########################################################################
from random import randint
from src.Simulation.factory.CRoverFactory import CRoverFactory

class CSimulation:
	def __init__(self, CParam):
		# Initialisation des Attributs
		self.days = 0 # 1 annee 668 jours
		self.hour = 0 
		self.parameters = CParam
		self.factory = CRoverFactory()
		self.is_sandstorm = False # wheels, camera, arm, solar panels, frame, antenna
		self.sandstorm_intensity = 1
		self.is_solarstorm = False # camera, cell, solar panels, antenna
		self.solarstorm_intensity = 1
		self.temp = -63

	def update_hour(self):
		# Mets a jour la simulation pour chaque heure
		self.is_storm()
	
		#Fais les degats au Rover
		self.apply_damage()

		# Mets a jour la temperature.
		self.update_temp()

		#Gestion du temp
		self.hour+=1
		if self.hour == 24:
			self.hour = 0
			self.update_day()
	
	def update_day(self):
		# Mets a jour la simulation pour chaque jour
		self.days += 1
	
	def is_storm(self):
		# Calcul le probabilite d'appartion ou disparition d'une tempete (sable/solaire)
		# Tempête Solaire
		solar_prob = randint(0,100)
		if not self.is_solarstorm: #Si pas de tempete
			if self.parameters.solarstorm_probability_spawn <= solar_prob: # On regarde la proba d'une apparition
				self.is_solarstorm = True
				self.solarstorm_intensity = randint(1,10)
		else:
			if self.parameters.solarstorm_probability_despawn <= solar_prob: # Sinon de disparition
				self.is_solarstorm = False

		# Tempête Sable
		sand_prob = randint(0,100)
		if not self.is_sandstorm:
			if self.parameters.sandstorm_probability_spawn <= sand_prob:
				self.is_sandstorm = True
				self.sandstorm_intensity = randint(1,10)
		else:
			if self.parameters.sandstorm_probability_despawn <= sand_prob:
				self.is_sandstorm = False

	def apply_damage(self):
		# applique les dégats a chaque rover
		for rover in self.factory.ls_rover:
			if self.is_sandstorm:
				rover.apply_damage_sandstorm(self.parameters.sandstorm_damage, self.sandstorm_intensity, self.temp)
			if self.is_solarstorm:
				rover.apply_damage_solarstorm(self.parameters.solarstorm_damage, self.solarstorm_intensity, self.temp)

			ls_damage = [self.parameters.wheel_damage,
						self.parameters.arm_damage,
						self.parameters.frame_damage,
						self.parameters.camera_damage,
						self.parameters.solar_panel_damage,
						self.parameters.cell_damage,
						self.parameters.antenna_damage]
			rover.apply_damage_global(ls_damage, self.temp)
			
	def update_temp(self):
		# Update la temperature
		if self.hour <= 12: # augemente entre minuit et midi 
			if self.temp != self.parameters.maxtemp: # si la temp n'est pas encore au max
				self.temp += randint(0,20) # on l'augemente entre 0 et 20 
				if self.temp > self.parameters.maxtemp: # si on a depasse le max, temp = max_temp
					self.temp = self.parameters.maxtemp
		else: #diminue entre minuit et midi 
			if self.temp != self.parameters.mintemp: 
				self.temp -= randint(0,20) 
				if self.temp < self.parameters.mintemp: 
					self.temp = self.parameters.mintemp


	def is_end(self):
		# Méthode qui vérifit si la limite en jour de la simulation à était atteinte
		print("jour: ", self.days)
		print("max jour: ", self.parameters.maxdays)
		if self.days >= self.parameters.maxdays:
			return True
		else:
			return False

	def afficher(self):
		print("========== ÉTAT DE LA SIMULATION ==========")
		print(f"Jour martien (sol)         : {self.days}")
		print(f"Heure                      : {self.hour}h")
		print(f"Température actuelle       : {self.temp}°C")
		print(f"Tempête de sable           : {'Oui' if self.is_sandstorm else 'Non'}")
		if self.is_sandstorm:
			print(f"  → Intensité              : {self.sandstorm_intensity}")
		print(f"Tempête solaire            : {'Oui' if self.is_solarstorm else 'Non'}")
		if self.is_solarstorm:
			print(f"  → Intensité              : {self.solarstorm_intensity}")
		
		print("========== ÉTAT DES ROVERS ==========")
		if not self.factory.ls_rover:
			print("Aucun rover dans la simulation.")
		else:
			self.factory.show_status_rover()
		print("====================================\n")

if __name__ == "__main__":
	from src.Parameters.CParameter import CParameter
	cp = CParameter()
	s = CSimulation(cp)

	for _ in range(5):
		s.update_hour()
		s.afficher()

