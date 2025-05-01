########################################################################
# Fichier qui vient Contenir la Classe de l'interface graphique de la Simulation
# Initialiser dans User
########################################################################

from src.Simulation.Controler.CSimulationCTRL import CSimulationCTRL

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
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

		# head info
		self.init_layout_head_info()

		# tab Rover
		self.init_tab_rover()
		# label
		self.stringallrover = ""
		self.tabstringrover = [""]
		self.lslabelrover = []
		self.init_label_log_rover()
		self.add_label_rover()

		# button
		self.init_layout_button()

	##### Initialisation Layout #####

	def init_layout(self):
		# Méthode pour initialiser le layout

		self.layout = QVBoxLayout()

		self.layouthead_info = QHBoxLayout()
		self.layoutscroll = QHBoxLayout()
		self.layoutbutton = QHBoxLayout()

		self.layout.addLayout(self.layouthead_info)
		self.layout.addLayout(self.layoutscroll)
		self.layout.addLayout(self.layoutbutton)

		self.setLayout(self.layout)

	#############################################

	def init_layout_head_info(self):
		# Méthode pour initialiser le layout des info d'entête

		# Météo
		self.labelmeteo = QLabel(f"Meteo: {self.CTRL.get_meteo(self.activ_sim)}")
		self.labelmeteo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
		self.layouthead_info.addWidget(self.labelmeteo)
		# Jour
		self.labelday = QLabel(f"Days: {self.CTRL.get_day(self.activ_sim)}")
		self.labelday.setAlignment(Qt.AlignmentFlag.AlignTop)
		self.layouthead_info.addWidget(self.labelday)
		# Heure
		self.labelhour = QLabel(f"hour: {self.CTRL.get_hour(self.activ_sim)}")
		self.labelhour.setAlignment(Qt.AlignmentFlag.AlignTop)	
		self.layouthead_info.addWidget(self.labelhour)	
		# NB Rover
		self.labelnbrover = QLabel(f"nb Rover: {self.CTRL.get_nbrover(self.activ_sim)}")
		self.labelnbrover.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
		self.layouthead_info.addWidget(self.labelnbrover)

	#### Initialisation Label Rover ####
	def init_label_log_rover(self):
		# Méthode pour initialiser le label log_rover

		# On initialise la zone Scrollable
		self.scroll = QScrollArea()

		# On initialise le Widget
		self.labeltext = QLabel(self.stringallrover)
		# On position en haut à gauche
		self.labeltext.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

		self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
		self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
		self.scroll.setWidgetResizable(True)
		
		self.scroll.setWidget(self.labeltext)

		# On l'ajoute au tab
		self.tab.addTab(self.scroll, "All")

	#### Initialisation Tab Rover ####
	def init_tab_rover(self):
		# Méthode pour initialiser le tab Rover
		self.tab = QTabWidget()
		self.layoutscroll.addWidget(self.tab)


	#### Initialisation Layout Button ####
	def init_layout_button(self):
		# Méthode pour initialiser le layout des Button

		# Menu
		# A Remplacer par un autre Layout
		self.init_menu()

		# button_rover
		self.button_create_Rover()
		# button reset
		self.button_reset_Sim()
		# button launch sim
		self.button_launch_Sim()

	#### Initialisation Menu ####
	def init_menu(self):
		# Méthode pour initialiser le Menu

		menu = self.CTRL.main_window.menuBar()

		# Save
		save_button = QAction("Save", self)
		save_button.triggered.connect(self.save_button)

		save_menu = menu.addMenu("Save")
		save_menu.addAction(save_button)
		save_menu.addSeparator()

		# Load
		load_button = QAction("Load", self)
		load_button.triggered.connect(self.load_button)

		load_menu = menu.addMenu("Load")
		load_menu.addAction(load_button)
		load_menu.addSeparator()

		# Retour Menu
		back_button = QAction("Back Main Menu", self)
		back_button.triggered.connect(self.back_button)

		back_menu = menu.addMenu("Back Main Menu")
		back_menu.addAction(back_button)

	#############################################

	# Setter
	def set_activ_sim(self, i):
		# Méthode pour changer la simulation gérer par le GUI
		self.activ_sim = i

	def add_log(self, string):
		# Méthode pour ajouter un log au label
		self.stringallrover += string
		self.labeltext.setText(self.stringallrover)

	def add_log_rover(self, string, i):
		# Méthode pour ajouter un log dans le label du i rover
		self.tabstringrover[i] += string
		self.lslabelrover[i].setText(self.tabstringrover[i])

	def reset_log(self):
		# Méthode pour resert le log label
		self.stringallrover = ""
		self.labeltext.setText(self.stringallrover)

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
		# On appel la méthode de CTRL
		self.CTRL.create_Rover(self.activ_sim)
		# On ajoute un nouveau string à remplir
		self.tabstringrover += [""]
		# On appel l'ajout de label rover
		self.add_label_rover()
		# On update l'header
		self.update_head()

	def add_label_rover(self):
		# Méthode pour ajouter un label rover est le link aux tab
		# On l'ajoute
		self.lslabelrover += [QLabel(self.tabstringrover[-1])]
		# On paramètre le dernier
		self.lslabelrover[-1].setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
		# On créer la Scroll Area

		scroll = QScrollArea()
		scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
		scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
		scroll.setWidgetResizable(True)
		
		scroll.setWidget(self.lslabelrover[-1])
		# On l'ajoute au tab
		self.tab.addTab(scroll, f"Rover{len(self.lslabelrover)}")

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
		# On reset le log
		self.reset_log()
		# On call la Method du CTRL
		self.CTRL.reset_simulation(self.activ_sim)
		# On update l'header
		self.update_head()

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
		self.CTRL.update_loop(self, self.activ_sim)

	#############################################

	def update_head(self):
		# Méthode pour update l'interface
		self.labelmeteo.setText(f"Meteo: {self.CTRL.get_meteo(self.activ_sim)}")
		self.labelday.setText(f"Days: {self.CTRL.get_day(self.activ_sim)}")
		self.labelhour.setText(f"hour: {self.CTRL.get_hour(self.activ_sim)}")
		self.labelnbrover.setText(f"nb Rover: {self.CTRL.get_nbrover(self.activ_sim)}")

	##### Menu Button ####
	def save_button(self):
		# Méthode pour gérer l'action du boutton save menu
		pass

	def load_button(self):
		# Méthode pour gérer l'action du boutton save menu
		pass

	def back_button(self):
		# Méthode pour gérer l'action du boutton save menu
		self.CTRL.back_menu()

