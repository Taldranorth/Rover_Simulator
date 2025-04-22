########################################################################
# Fichier qui vient Contenir la Classe Composants
########################################################################

class CComponents:
	def __init__(self, nm, rs):
		# Initialisation des Attributs
		# Nom du Composants
		name = nm
		# États du Composants en %
		durability = 100
		# Résistance
		resistance = rs

	def damage_durability(self, change):
		# Méthode pour abimer la durabilité du composants selon la résistance
		durability = change*(self.resistance/100)

	def change_durability(self, change):
		# Méthode pour changer la durabilité selon la résistance
		durability = change


	def change_resistance(self, change):
		# Méthode pour changer la résistance du Composants
		resistance = change

