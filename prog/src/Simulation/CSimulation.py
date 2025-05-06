########################################################################
# Fichier qui vient Contenir la Classe de la Simulation
# Initialiser dans Server
########################################################################
import sys
from io import StringIO
from random import randint

from src.Simulation.factory.CRoverFactory import CRoverFactory
from src.Simulation.CRover import  CRover

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

		self.delays = 1
		# Attributs pour stocker les données
		self.history = {"meteo":[],"temperature":[],"roveralive":[]}

	def update_hour(self):
		# Mets a jour la simulation pour chaque heure
		self.is_storm()
	
		#Fais les degats au Rover
		self.apply_damage()

		# Mets a jour la temperature.
		self.update_temp()
		# Mets à jour l'historique
		self.update_history()
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
			if rover.dead == False:
				if self.is_sandstorm:
					rover.apply_damage_sandstorm(self.parameters.sandstorm_damage, self.sandstorm_intensity, self.temp)
				if self.is_solarstorm:
					rover.apply_damage_solarstorm(self.parameters.solarstorm_damage, self.solarstorm_intensity, self.temp)

				ls_damage = []
				for string in ["wheel","arm","frame","camera","solar_panel","cell","antenna"]:
					ls_damage += [self.parameters.get_components_damage(string)]
				rover.apply_damage_global(ls_damage, self.temp)
				rover.is_dead()
			
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

	def update_history(self):
		# Update l'historique
		# Meteo
		if self.is_sandstorm == True:
			self.history["meteo"] += ["SandStorm"]
		elif self.is_solarstorm == True:
			self.history["meteo"] += ["SolarStorm"]
		else:
			self.history["meteo"] += ["Clear"]

		# Température
		self.history["temperature"] += [self.temp]
		# nb Rover alive
		self.history["roveralive"] += [self.factory.get_alive_rover()]



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

	def get_rover_log(self):
		# Méthode qui renvoit afficher mais dans un str
		# bourine est à remplacer plus tard
		# On garde en mémoire la sortie terminal
		old_stdout = sys.stdout
		# On prépare la variable de stockage
		result = StringIO()
		# on change la sortie standart par la variable
		sys.stdout = result
		# on remplit
		self.afficher()
		# on remet l'ancienne sortie terminal
		sys.stdout = old_stdout
		# on retourne la variable
		return result.getvalue()

	def get_single_rover_log(self, i):
		# Méthode qui renvoit les données d'un unique rover
		old_stdout = sys.stdout
		result = StringIO()
		sys.stdout = result
		self.factory.show_status_rover_single(i)
		sys.stdout = old_stdout
		return result.getvalue()

	def get_history_rover(self, irover):
		#
		return self.factory.get_history_rover(irover)


	def create_Rover(self):
		# Méthode pour appeler la création d'un rover
		self.factory.create_Rover()
		# On applique les paremètres de la Simulation
		self.factory.load_parameters_rover(self.parameters, self.factory.get_nbrover()-1)


	def get_meteo(self):
		# Méthode retourne la météo
		if self.is_sandstorm == True:
			return "SandStorm"
		elif self.is_solarstorm == True:
			return "SolarStorm"
		else:
			return "Clear"

	def get_day(self):
		# Méthode retourne le jour
		return self.days

	def get_hour(self):
		# Méthode retourne l'heure
		return self.hour

	def get_nbrover(self):
		# Méthode retourne le nombre de Rover
		return self.factory.get_nbrover()

	def get_alive_rover(self):
		# Méthode qui retourne le nb de rover en vie
		return self.factory.get_alive_rover()

	def get_temp(self):
		# Méthode qui retourne la temp de la simulation
		return self.temp

	def get_components_durability_all(self, irover):
		return self.factory.get_components_durability_all(irover)

	def get_history_rover(self, irover):
		return self.factory.get_history_rover(irover)

	def get_history_simulation(self):
		return self.history

	#### Save/Load ####
	def to_dict(self):
		# Méthode pour Sauvegarder dans un dico
		data = {
			"days": self.days,
			"hour": self.hour,
			"sandstorm":{
				"is_sandstorm": self.is_sandstorm,
				"intensity": self.sandstorm_intensity
			},
			"solarstorm":{
				"is_solarstorm": self.is_solarstorm,
				"intensity": self.solarstorm_intensity
			},
			"temp": self.temp,
			"history":self.history,
			#save les rovers et leur états
			"rovers": [rover.to_dict() for rover in self.factory.ls_rover]
			
		}
		return data



	def from_dict(self, data):
		# Méthode pour Charger depuis un dico
		self.days = data["days"]
		self.hour = data["hour"]
		
		self.is_sandstorm = data["sandstorm"]["is_sandstorm"]
		self.sandstorm_intensity = data["sandstorm"]["intensity"]
		
		self.is_solarstorm = data["solarstorm"]["is_solarstorm"]
		self.solarstorm_intensity = data["solarstorm"]["intensity"]
		
		self.temp = data["temp"]
		self.history = data["history"]
		
		#charger les rover et leur etat
		self.factory.load_rovers_from_dict(data.get("rovers", []))



