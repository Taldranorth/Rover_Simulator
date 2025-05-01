########################################################################
# Fichier qui vient Contenir la Classe de l'interface graphique de la Simulation
# Initialiser dans User
########################################################################

from src.Simulation.Controler.CSimulationCTRL import CSimulationCTRL

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTabWidget, QScrollArea

class CSimulationGUI(QWidget):
	def __init__(self, main_window, sim_factory, param_factory):
		# On initialise la classe hérité
		super().__init__()
		# On setup le layout
		self.init_layout()
		# On initialise les attributs du Widget
		# le Controler
		self.CTRL = CSimulationCTRL(main_window, sim_factory, param_factory)
		# Simulation actuelle
		self.activ_sim = 0

		# test
		self.stringtest = ""
		self.init_label_log_rover()

		# button_rover
		self.button_create_Rover()
		# button reset
		self.button_reset_Sim()
		# button launch sim
		self.button_launch_Sim()

	##### Initialisation Layout #####

	def init_layout(self):
		# Méthode pour initialiser le layout

		self.layout = QVBoxLayout()
		self.layoutbutton = QHBoxLayout()
		self.layout.addLayout(self.layoutbutton)

		self.setLayout(self.layout)

	#############################################

	#### Initialisation Label Rover ####
	def init_label_log_rover(self):
		# Méthode pour initialiser le label log_rover

		# On initialise la zone Scrollable
		self.scroll = QScrollArea()

		# On initialise le Widget
		self.labeltext = QLabel(self.stringtest)
		# On position en haut à gauche
		self.labeltext.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
		self.scroll.setWidgetResizable(True)
		
		self.scroll.setWidget(self.labeltext)

		# On ajoute au layout
		self.layout.addWidget(self.scroll)

	#############################################

	# Setter
	def set_activ_sim(self, i):
		# Méthode pour changer la simulation gérer par le GUI
		self.activ_sim = i

	def add_log(self, string):
		# Méthode pour ajouter un log au label
		self.stringtest += string
		self.labeltext.setText(self.stringtest)

	def reset_log(self):
		# Méthode pour resert le log label
		self.stringtest = ""
		self.labeltext.setText(self.stringtest)

	#############################################

	#### Button Create Rover ####
	def button_create_Rover(self):
		# Méthode pour créer un button qui appeler la création d'un rover
		button = QPushButton("Create Rover")
		# On set l'action
		button.clicked.connect(self.button_create_Rover_clicked)
		# On ajoute au layoutbutton
		self.layoutbutton.addWidget(button)

	def button_create_Rover_clicked(self):
		# Méthode retour utilisateur quand le boutton est cliqué
		self.CTRL.create_Rover(self.activ_sim)

	#############################################

	#### Button Reset Sim ####
	def button_reset_Sim(self):
		# Méthode pour créer un button qui appeler la création d'un rover
		button = QPushButton("Reset Sim")
		# On set l'action
		button.clicked.connect(self.button_reset_Sim_clicked)
		# On ajoute au layoutbutton
		self.layoutbutton.addWidget(button)

	def button_reset_Sim_clicked(self):
		# Méthode retour utilisateur quand le boutton est cliqué
		print("Reset la Simulation N°",self.activ_sim)
		# On supprime
		self.CTRL.remove_simulation(self.activ_sim)
		# On recréer
		self.CTRL.create_simulation(self.CTRL.get_parameter(0))
		# On reset le log
		self.reset_log()
		# On recréer un Rover
		self.CTRL.create_Rover(self.activ_sim)

	#############################################

	#### Button launch Sim ####
	def button_launch_Sim(self):
		# Méthode pour créer un button qui appeler la création d'un rover
		button = QPushButton("Launch Sim")
		# On set l'action
		button.clicked.connect(self.button_launch_Sim_clicked)
		# On ajoute au layoutbutton
		self.layoutbutton.addWidget(button)

	def button_launch_Sim_clicked(self):
		# Méthode retour utilisateur quand le boutton est cliqué
		print("On lance la Simulation")
		s = self.CTRL.get_simulation(0)
		while(s.is_end() == False):
			# On update
			s.update_hour()
			# On affiche dans le terminal
			s.afficher()
			# On redirige vers le Window text
			self.add_log(s.get_rover_log())

	#############################################


