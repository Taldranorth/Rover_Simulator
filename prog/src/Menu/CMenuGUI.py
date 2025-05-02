########################################################################
# Fichier qui vient Contenir la Classe de l'interface graphique du Menu
# Initialiser dans User
########################################################################

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTabWidget, QScrollArea, QDialog, QDialogButtonBox, QListWidget


from src.Menu.CMenuCTRL import CMenuCTRL
from src.Simulation.CData import scan_simulation_file

class CMenuGUI(QWidget):
	def __init__(self, main_window, sim_factory, param_factory):
		# On initialise la classe hérité
		super().__init__()
		# On setup le layout
		self.layout = 0
		self.init_layout(main_window)
		# On initialise les attributs du Widget
		self.CTRL = CMenuCTRL(main_window, sim_factory, param_factory)

	def init_layout(self, main_window):
		# Méthode pour initialiser le layout
		self.layout = QHBoxLayout()

		self.layoutbutton = QVBoxLayout()

		self.init_button(main_window)

		laytout_nothing = QVBoxLayout()
		self.layout.addLayout(self.layoutbutton)
		self.layout.addLayout(laytout_nothing)
		self.setLayout(self.layout)



	def init_button(self, main_window):
		# Méthode pour initialiser les bouttons

		# New Simulation
		button = QPushButton("New Simulation")
		button.clicked.connect(self.new_simulation_clicked)
		# On set l'alignement
		#button.setAlignment(Qt.AlignmentFlag.AlignLeft)
		self.layoutbutton.addWidget(button, alignment = Qt.AlignmentFlag.AlignLeft)

		# Load Simulation
		button = QPushButton("Load Simulation")
		button.clicked.connect(lambda: self.load_simulation_clicked(main_window))
		self.layoutbutton.addWidget(button, alignment = Qt.AlignmentFlag.AlignLeft)

		# Manage Result
		button = QPushButton("Manage Result")
		button.clicked.connect(self.manage_result_clicked)
		self.layoutbutton.addWidget(button, alignment = Qt.AlignmentFlag.AlignLeft)

		# Exit
		button = QPushButton("Exit")
		button.clicked.connect(self.exit_clicked)
		self.layoutbutton.addWidget(button, alignment = Qt.AlignmentFlag.AlignLeft)



	##### Button ####
	def new_simulation_clicked(self):
		# Méthode pour gérer le clicked sur le boutton new Sim
		self.CTRL.new_simulation()


	def load_simulation_clicked(self, main_window):
		# Méthode pour gérer le clicked sur le boutton load Simulation
		# On met en place l'interface de sélection des Sauvegardes
		self.dialog_load_simulation(main_window)


	def manage_result_clicked(self):
		# Méthode pour gérer le clicked sur le boutton manage result
		# On met en palce l'interface de sélection des résultats
		pass

	def exit_clicked(self):
		# Méthode pour gérer le clicked sur le boutton exit
		self.CTRL.exit()





	##### Load Simulation ####
	def dialog_load_simulation(self, main_window):
		# Méthode pour créer et afficher la window de chargement de simulation
		dlg = QDialog(main_window)
		dlg.setWindowTitle("Load Simulation")

		#### Set Layout ####
		global_layout = QVBoxLayout()
		button_layout = QHBoxLayout()

		Qlist = QListWidget()
		self.dialog_init_list(Qlist)
		global_layout.addWidget(Qlist)
		global_layout.addLayout(button_layout)

		#### Set Button ####
		# Open
		button = QPushButton("Open")
		button.clicked.connect(lambda: self.dialog_load(dlg, Qlist))
		button_layout.addWidget(button)
		# Cancel
		button = QPushButton("Cancel")
		button.clicked.connect(lambda: self.dialog_exit(dlg))
		button_layout.addWidget(button)


		dlg.setLayout(global_layout)
		dlg.exec()

	def dialog_init_list(self, Qlist):
		# Méthode liées au dialogue load Simulation
		# On recup la liste des fichiers dans le dossiers des Simulation
		ls_file = scan_simulation_file()
		# On créer la liste
		Qlist.addItems(ls_file)


	def dialog_load(self, dlg, Qlist):
		# Méthode liées au button load du dialog load Simulation
		print("objet actuelle:", Qlist.currentItem().text())
		# On recup le nom
		filename = Qlist.currentItem().text()
		# On le balance au Controler
		self.CTRL.load_simulation(filename)
		# On ferme la fenêtre
		dlg.close()


	def dialog_exit(self, dlg):
		# Méthode liées au button exit du dialog load Simulation
		dlg.close()





