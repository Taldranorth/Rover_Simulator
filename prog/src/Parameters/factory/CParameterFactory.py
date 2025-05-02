########################################################################
# Fichier qui vient Contenir la Classe Factory des Paramètres
# Initialiser dans Server
########################################################################

from src.Parameters.CParameter import CParameter
from src.Simulation.CData import CData

class CParameterFactory:
	def __init__(self):
		self.ls_parameter = []
		self.nb = 0

	def get_parameter(self, i):
		# Méthode pour retourner l'objet parameter
		return self.ls_parameter[i]

	def create_parameter(self):
		# Méthode pour ajouter une parameter
		parameter = CParameter()
		self.ls_parameter += [parameter]
		self.nb += 1

	def remove_parameter(self, i):
		# Méthode pour retirer une parameter
		self.ls_parameter = self.ls_parameter[:i] + self.ls_parameter[i+1:]
		self.nb -=1


	def save_parameters(self, i, filename):
		#
		data = self.ls_parameter[i].to_dict()
		#
		cdata = CData()
		cdata.save_parameters(data, filename)

	def load_parameters(self, i, filename):
		#
		cdata = CData()
		data = cdata.load_parameters(filename)
		if data:
			self.ls_parameter[i].from_dict(data)


	#### Setter ####

	def set_maxdays(self, i, change):
		# Méthode pour set le max days
		self.ls_parameter[i].set_maxdays(change)

	# Météo
	# Sandstorm
	def set_sandstorm_probability_spawn(self, i, change):
		# Méthode pour set la probabilité de spawn d'une tempête de sable
		self.ls_parameter[i].set_sandstorm_probability_spawn(change)

	def set_sandstorm_probability_despawn(self, i, change):
		# Méthode pour set la probabilité de despawn d'une tempête de sable
		self.ls_parameter[i].set_sandstorm_probability_despawn(change)

	def set_sandstorm_damage(self, i, change):
		# méthode pour set les dégâts d'une tempête de sable
		self.ls_parameter[i].set_sandstorm_damage(change)

	# SolarSorm
	def set_solarstorm_probability_spawn(self, i, change):
		# Méthode pour set la probabilité de spawn d'une tempête de sable
		self.ls_parameter[i].set_solarstorm_probability_spawn(change)

	def set_solarstorm_probability_despawn(self, i, change):
		# Méthode pour set la probabilité de despawn d'une tempête de sable
		self.ls_parameter[i].set_solarstorm_probability_despawn(change)

	def set_solarstorm_damage(self, i, change):
		# méthode pour set les dégâts d'une tempête de sable
		self.ls_parameter[i].set_solarstorm_probability_damage(change)

	# Température
	def set_maxtemp(self, i, change):
		# Méthode pour set la température max
		self.ls_parameter[i].set_maxtemp(change)

	def set_mintemp(self, i, change):
		# Méthode pour set la température min
		self.ls_parameter[i].set_mintemp(change)

	# Composants

	def set_components_durability(self, i, components, change):
		# Méthode pour set la durabilité d'un composants
		self.ls_parameter[i].set_components_durability(components, change)

	def set_components_resistance(self, i, components, change):
		# Méthode pour set la résistance d'un composants
		self.ls_parameter[i].set_components_resistance(components, change)

	def set_components_damage(self, i, components, change):
		# Méthode pour set les dégâts du composants pris par tour
		self.ls_parameter[i].set_components_damage(components, change)


