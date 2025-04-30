########################################################################
# Fichier qui vient Contenir la Classe Controller des Paramètres
# Initialiser dans Server
########################################################################




class CParameterCTRL:
	def __init__(self, param_factory):
		self.param_factory = param_factory

	def create_parameter(self):
		# Méthode pour ajouter une simulation par la méthode de la factory
		self.param_factory.create_parameter()

	def remove_parameter(self, i):
		# Méthode pour retirer une simulation
		self.param_factory.remove_parameter(i)

	def get_parameter(self, i):
		# Méthode pour récupérer l'objet SImulation à la I place
		return self.param_factory.get_parameter(i)




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


