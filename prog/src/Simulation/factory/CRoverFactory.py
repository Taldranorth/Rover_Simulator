########################################################################
# Fichier qui vient Contenir la Classe Factory des Rover
# Initialiser dans Server
########################################################################
from src.Simulation.CRover import CRover

class CRoverFactory:
	def __init__(self):
		self.ls_rover = []
		self.nb = 0

	def get_Rover(self, i):
		# Méthoder pour récuperer le i rover
		return self.ls_rover[i]


	def create_Rover(self):
		# Méthode pour ajouter un rover
		print("On créer le Rover N°",self.nb+1)
		rover = CRover()
		self.ls_rover += [rover]
		self.nb += 1

	def remove_Rover(self, i):
		# Méthode pour retirer un rover
		self.ls_rover = self.ls_rover[:i] + self.ls_rover[i+1:]

	def show_status_rover_single(self, i):
		# Méthode pour afficher le status d'un unique Rover
		print(f"[Rover {i}] Nom : {self.ls_rover[i].name if hasattr(rover, 'name') else 'Inconnu'}")
		if hasattr(self.ls_rover[i], 'show_status'):  # Si le rover a une méthode de status
			print(self.ls_rover[i].show_status())		

	def show_status_rover(self):
		# Méthode pour afficher le status de tout les Rovers

		for i, rover in enumerate(self.ls_rover):
			print(f"[Rover {i+1}] Nom : {rover.name if hasattr(rover, 'name') else 'Inconnu'}")
			if hasattr(rover, 'show_status'):  # Si le rover a une méthode de status
				print(rover.show_status())
