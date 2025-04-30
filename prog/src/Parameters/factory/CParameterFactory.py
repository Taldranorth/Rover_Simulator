########################################################################
# Fichier qui vient Contenir la Classe Factory des Paramètres
# Initialiser dans Server
########################################################################

from src.Parameters.CParameter import CParameter


class CParameterFactory:
	def __init__(self):
		self.ls_parameter = []

	def get_parameter(self, i):
		# Méthode pour retourner l'objet parameter
		return self.ls_parameter[i]

	def create_parameter(self):
		# Méthode pour ajouter une parameter
		parameter = CParameter()
		self.ls_parameter += [parameter]

	def remove_parameter(self, i):
		# Méthode pour retirer une parameter
		self.ls_parameter = self.ls_parameter[:i] + self.ls_parameter[i+1:]