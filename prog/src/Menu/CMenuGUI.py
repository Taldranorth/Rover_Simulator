########################################################################
# Fichier qui vient Contenir la Classe de l'interface graphique du Menu
# Initialiser dans User
########################################################################

from src.Menu.CMenuCTRL import CMenuCTRL
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout

class CMenuGUI(QWidget):
	def __init__(self):
		# On initialise la classe hérité
		super().__init__()
		# On setup le layout
		self.layout = 0
		self.init_layout()
		# On initialise les attributs du Widget



	def init_layout(self):
		# Méthode pour initialiser le layout
		self.layout = QHBoxLayout()
		self.setLayout(self.layout)

