########################################################################
# Fichier qui vient Contenir la Classe Controller des Paramètres
# Initialiser dans Users
########################################################################
from src.Simulation.CData import CData

class CParameterCTRL:
	def __init__(self, main_window, sim_factory, param_factory):
		# link vers la window
		self.main_window = main_window
		# link vers la factory
		self.sim_factory = sim_factory
		self.param_factory = param_factory



	# Simulation
	def create_simulation(self, CParam):
		# Méthode pour ajouter une simulation par la méthode de la factory
		self.sim_factory.create_simulation(CParam)

	def remove_simulation(self, i):
		# Méthode pour retirer une simulation
		self.sim_factory.remove_simulation(i)

	def get_simulation(self, i):
		# Méthode pour récupérer l'objet SImulation à la I place
		return self.sim_factory.get_simulation(i)

	def create_Rover(self, i):
		# Méthode pour appeler la création d'un rover dans I ième simulation de la liste
		self.sim_factory.create_Rover(i)

	# Parameter
	def create_parameter(self):
		# Méthode pour ajouter une simulation par la méthode de la factory
		self.param_factory.create_parameter()

	def remove_parameter(self, i):
		# Méthode pour retirer une simulation
		self.param_factory.remove_parameter(i)

	def get_parameter(self, i):
		# Méthode pour récupérer l'objet SImulation à la I place
		return self.param_factory.get_parameter(i)

	#### Getter ####
	def get_maxdays(self, i):
		return self.param_factory.get_maxdays(i)

	def get_sandstorm_probability_spawn(self, i):
		return self.param_factory.get_sandstorm_probability_spawn(i)

	def get_sandstorm_probability_despawn(self, i):
		return self.param_factory.get_sandstorm_probability_despawn(i)

	def get_sandstorm_damage(self, i):
		return self.param_factory.get_sandstorm_damage(i)

	def get_solarstorm_probability_spawn(self, i):
		return self.param_factory.get_solarstorm_probability_spawn(i)

	def get_solarstorm_probability_despawn(self, i):
		return self.param_factory.get_solarstorm_probability_despawn(i)

	def get_solarstorm_damage(self, i):
		return self.param_factory.get_solarstorm_damage(i)

	def get_mintemp(self, i):
		return self.param_factory.get_mintemp(i)

	def get_maxtemp(self, i):
		return self.param_factory.get_maxtemp(i)

	def get_components_durability(self, i, components):
		return self.param_factory.get_components_durability(i, components)

	def get_components_resistance(self, i, components):
		return self.param_factory.get_components_resistance(i, components)

	def get_components_damage(self, i, components):
		return self.param_factory.get_components_damage(i, components)

	#### Setter ####

	def set_maxdays(self, i, change):
		# Méthode pour set le max days
		self.param_factory.set_maxdays(i, change)

	# Météo
	# Sandstorm
	def set_sandstorm_probability_spawn(self, i, change):
		# Méthode pour set la probabilité de spawn d'une tempête de sable
		self.param_factory.set_sandstorm_probability_spawn(i, change)

	def set_sandstorm_probability_despawn(self, i, change):
		# Méthode pour set la probabilité de despawn d'une tempête de sable
		self.param_factory.set_sandstorm_probability_despawn(i, change)

	def set_sandstorm_damage(self, i, change):
		# méthode pour set les dégâts d'une tempête de sable
		self.param_factory.set_sandstorm_damage(i, change)

	# SolarSorm
	def set_solarstorm_probability_spawn(self, i, change):
		# Méthode pour set la probabilité de spawn d'une tempête de sable
		self.param_factory.set_solarstorm_probability_spawn(i, change)

	def set_solarstorm_probability_despawn(self, i, change):
		# Méthode pour set la probabilité de despawn d'une tempête de sable
		self.param_factory.set_solarstorm_probability_despawn(i, change)

	def set_solarstorm_damage(self, i, change):
		# méthode pour set les dégâts d'une tempête de sable
		self.param_factory.set_solarstorm_probability_damage(i, change)

	# Température
	def set_maxtemp(self, i, change):
		# Méthode pour set la température max
		self.param_factory.set_maxtemp(i, change)

	def set_mintemp(self, i, change):
		# Méthode pour set la température min
		self.param_factory.set_mintemp(i, change)

	# Composants

	def set_components_durability(self, i, components, change):
		# Méthode pour set la durabilité d'un composants
		self.param_factory.set_components_durability(i, components, change)

	def set_components_resistance(self, i, components, change):
		# Méthode pour set la résistance d'un composants
		self.param_factory.set_components_resistance(i, components, change)

	def set_components_damage(self, i, components, change):
		# Méthode pour set les dégâts du composants pris par tour
		self.param_factory.set_components_damage(i, components, change)


	#### Button ####
	def launch_sim(self, i):
		# Méthode pour gérer l'appel du Boutton launch Simulation
		# On créer l'instance de la simulation
		self.main_window.widget.CTRL.create_simulation(self.get_parameter(i))
		
		# On change la fenêtre
		self.main_window.change_GUI("CSimulationGUI")

	def back(self):
		# Méthode pour gérer l'appel du Button Back
		self.main_window.change_GUI("CMenuGUI")

	def save_preset(self, i, filename):
		# Méthode pour gérer l'appel du Button Save Preset
		self.param_factory.save_parameters(i,filename)

	def load_preset(self, i, filename):
		# Méthode pour gérer l'appel du Button Load Preset
		self.param_factory.load_parameters(i,filename)
