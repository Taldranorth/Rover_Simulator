########################################################################
# Fichier qui vient Contenir la Classe de l'interface graphique du Menu
# Initialiser dans User
########################################################################

from src.Menu.CMenuCTRL import CMenuCTRL
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTabWidget, QScrollArea

class CMenuGUI(QWidget):
	def __init__(self, main_window, sim_factory, param_factory):
		# On initialise la classe hérité
		super().__init__()
		# On setup le layout
		self.layout = 0
		self.init_layout()
		# On initialise les attributs du Widget
		self.CTRL = CMenuCTRL(main_window, sim_factory, param_factory)

	def init_layout(self):
		# Méthode pour initialiser le layout
		self.layout = QHBoxLayout()

		self.layoutbutton = QVBoxLayout()

		self.init_button()

		laytout_nothing = QVBoxLayout()
		self.layout.addLayout(self.layoutbutton)
		self.layout.addLayout(laytout_nothing)
		self.setLayout(self.layout)



	def init_button(self):
		# Méthode pour initialiser les bouttons

		# New Simulation
		button = QPushButton("New Simulation")
		button.clicked.connect(self.new_simulation_clicked)
		self.layoutbutton.addWidget(button)

		# Load Simulation
		button = QPushButton("Load Simulation")
		button.clicked.connect(self.load_simulation_clicked)
		self.layoutbutton.addWidget(button)

		# Manage Result
		button = QPushButton("Manage Result")
		button.clicked.connect(self.manage_result_clicked)
		self.layoutbutton.addWidget(button)

		# Exit
		button = QPushButton("Exit")
		button.clicked.connect(self.exit_clicked)
		self.layoutbutton.addWidget(button)



	##### Button ####
	def new_simulation_clicked(self):
		# Méthode pour gérer le clicked sur le boutton new Sim
		self.CTRL.new_simulation()


	def load_simulation_clicked(self):
		# Méthode pour gérer le clicked sur le boutton load Simulation
		# On met en place l'interface de sélection des Sauvegardes
		pass


	def manage_result_clicked(self):
		# Méthode pour gérer le clicked sur le boutton manage result
		# On met en palce l'interface de sélection des résultats
		pass

	def exit_clicked(self):
		# Méthode pour gérer le clicked sur le boutton exit
		pass

