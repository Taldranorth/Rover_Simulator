########################################################################
# Fichier qui vient Contenir la Classe de la Simulation
########################################################################
from random import randint
from src.Simulation.Factory.CRoverFactory import CRoverFactory

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
		if not self.is_sand_torm:
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
				rover.apply_damage_sandstorm(self.parameters.sandstorm_damage, self.sandstorm_intensity)
			if self.is_solarstorm:
				rover.apply_damage_solarstorm(self.parameters.solarstorm_damage, self.solarstorm_intensity)
			rover.apply_global_damage(self.parameters.global_damage)
			

