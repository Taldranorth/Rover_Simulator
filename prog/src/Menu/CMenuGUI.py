########################################################################
# Fichier qui vient Contenir la Classe de l'interface graphique du Menu
########################################################################

# Classe Principale de la fenêtre de l'application

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow

class CMenuGUI(QMainWindow):
	def __init__(self):
		# Initialiser la classe hérité
		super().__init__()
		# Initialise le titre
		window.setWindowTitle("Test Simulateur de Rover")

		pass




	# Setter
	def set_window_size(self, Width, Height):
		# Méthode pour set la hauteur et la largeur de la window
		window.setFixedSize(Width, Height)

