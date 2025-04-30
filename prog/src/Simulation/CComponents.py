########################################################################
# Fichier qui vient Contenir la Classe Composants
# Initialiser dans Server
########################################################################
#ajouter gestion des dégats selon la température



class CComponents:
	def __init__(self, nm, rs):
		# Initialisation des Attributs
		# Nom du Composants
		self.name = nm
		# États du Composants en %
		self.durability = 100
		# Résistance
		self.resistance = rs
		#Range température du Composant
		self.maxtemp = 20
		self.mintemp = -143

	def damage_durability(self, change, temperature):
		# Méthode pour abimer la durabilité du composants selon la résistance

		#### Calcule de l'effet de la température ####
		temp_effect = 0
		if temperature < 0:
			temp_effect = temperature/self.mintemp
		else:
			temp_effect = temperature/self.maxtemp

		# Si l'effet de la température est minim ont met à 0
		if temp_effect < 0.5:
			temp_effect = 0


		#### Calcule de l'effet de la résistance ####
		effect = change*(self.resistance/100)

		#### On applique les dégâts ####
		self.durability -= (effect + (effect*temp_effect))


	# Setter
	def set_durability(self, change):
		# Méthode pour changer la durabilité
		self.durability = change

	def set_resistance(self, change):
		# Méthode pour changer la résistance du Composants
		self.resistance = change

	def set_maxtemp(self, change):
		# Méthode pour changer la température max du composant
		self.maxtemp = change

	def set_mintemp(self, change):
		# Méthode pour changer la température min du composant
		self.mintemp = change
