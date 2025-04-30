########################################################################
# Fichier qui vient Contenir la Classe de l'interface graphique de la Simulation
# Initialiser dans User
########################################################################

from src.Simulation.Controler.CSimulationCTRL import CSimulationCTRL

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QLabel

class CSimulationGUI(QWidget):
	def __init__(self, sim_factory, param_factory):
		# On initialise la classe hérité
		super().__init__()
		# On setup le layout
		self.layout = 0
		self.init_layout()
		# On initialise les attributs du Widget
		# le Controler
		self.CTRL = CSimulationCTRL(sim_factory, param_factory)

		# test
		self.stringtest = ""
		self.init_label_log_rover()

	def init_layout(self):
		# Méthode pour initialiser le layout
		self.layout = QHBoxLayout()
		self.setLayout(self.layout)



	def init_label_log_rover(self):
		# Méthode pour initialiser le label log_rover
		self.labeltext = QLabel(self.stringtest)
		# On position en haut à gauche
		self.labeltext.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
		# On ajoute au layout
		self.layout.addWidget(self.labeltext)

	def add_log(self, string):
		# Méthode pour ajouter un log au label
		self.stringtest += string
		self.labeltext.setText(self.stringtest)