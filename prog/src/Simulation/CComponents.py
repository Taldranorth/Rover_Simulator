########################################################################
# Fichier qui vient Contenir la Classe Composants
########################################################################

class CComposants:
	def __init__(self, nm, rs):
		# Initialisation des Attributs
		# Nom du Composants
		name = nm
		# États du Composants en %
		durability = 100
		# Résistance
		resistance = rs

	def change_durability(self, change):
		# Méthode pour changer la durabilité selon la résistance
		durability = change*(rs/100)

		
