########################################################################
# Fichier qui vient Contenir la Classe de l'interface graphique de la Simulation
# Initialiser dans User
########################################################################

from src.Simulation.Controler.CSimulationCTRL import CSimulationCTRL
from src.Simulation.CData import scan_simulation_file
from src.Display.plot import CGraph

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTabWidget, QScrollArea, QDialog, QListWidget, QLineEdit



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
		self.lstabrover = []
		self.init_tab_global()

		# button
		self.init_layout_button(main_window)

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
	def init_tab_global(self):
		# Méthode pour initialiser le tab rover all

		tab = QTabWidget()

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
		tab.addTab(self.scroll,"Global")

		# On initialise les tab Météo, température et rover
		for txt in ["meteo","temperature","rover"]:
			graph = CGraph(txt)
			tab.addTab(graph, txt)

		# On finit par ajouter le tab global
		self.tab.addTab(tab, "All Rover")

	#### Initialisation Tab Rover ####
	def init_tab_rover(self):
		# Méthode pour initialiser le tab Rover
		self.tab = QTabWidget()
		self.layoutscroll.addWidget(self.tab)

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
		# On l'ajoute au tab du rover
		self.lstabrover[-1].addTab(scroll, "Global")
		

	def add_tab_rover(self):
		# Méthode pour ajouter un tab de Rover
		# On créer le nouveaux tab
		self.lstabrover += [QTabWidget()]
		# On ajoute le nouveau tab au tab globale
		self.tab.addTab(self.lstabrover[-1],f"Rover{len(self.lslabelrover)}")


	def add_graphe_rover(self, irover, type):
		# Méthode pour ajouter un Graphe aux iRover
		# On créer le graphe
		graph = CGraph(type)
		# On l'ajoute au tableau du irover avec le bon titre
		if type == "meteo":
			self.lstabrover[irover].addTab(graph, "Graph meteo")
		elif type == "temperature":
			self.lstabrover[irover].addTab(graph, "Graph temperature")
		elif type == "components":
			self.lstabrover[irover].addTab(graph, "Graph components")
		elif type == "rover":
			self.lstabrover[irover].addTab(graph, "Graph rover")
		else:
			self.lstabrover[irover].addTab(graph, "Graph test")



	#### Initialisation Layout Button ####
	def init_layout_button(self, main_window):
		# Méthode pour initialiser le layout des Button

		# Menu
		# A Remplacer par un autre Layout
		self.init_menu(main_window)

		# button_rover
		self.button_create_Rover()
		# button reset
		self.button_reset_Sim()
		# button launch sim
		self.button_launch_Sim()
		# button stop
		self.button_stop()

	#### Initialisation Menu ####
	def init_menu(self, main_window):
		# Méthode pour initialiser le Menu

		menu = self.CTRL.main_window.menuBar()

		# Save
		save_button = QAction("Save", self)
		save_button.triggered.connect(lambda:  self.dialog_simulation(main_window, 1))

		save_menu = menu.addMenu("Save")
		save_menu.addAction(save_button)
		save_menu.addSeparator()

		# Load
		load_button = QAction("Load", self)
		load_button.triggered.connect(lambda:  self.dialog_simulation(main_window))

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
		self.stringallrover = string
		self.labeltext.setText(self.stringallrover)

	def add_log_rover(self, string, i):
		# Méthode pour ajouter un log dans le label du i rover
		self.tabstringrover[i] = string
		self.lslabelrover[i].setText(self.tabstringrover[i])

	def reset_log(self):
		# Méthode pour reset le log label
		self.stringallrover = ""
		self.labeltext.setText(self.stringallrover)
	
		for x in range(len(self.lslabelrover)):
			self.lslabelrover[x].setText("")
		self.tabstringrover = [""]
		self.lslabelrover = []

	def reset_tabrover(self):
		# Méthode pour reset le tab rover
		print("nettoyage tableau")
		self.tab.clear()
		self.lstabrover = []

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
		# On appel l'ajout d'un nouveau tab rover
		self.add_tab_rover()
		# On appel l'ajout de label rover
		self.add_label_rover()
		# On appel l'ajout de graph des rovers
		self.add_graphe_rover(len(self.lslabelrover)-1, "components")
		# On update l'header
		self.update_head()

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
		# On reset les log
		self.reset_log()
		# On reset le tableau des rover
		self.reset_tabrover()
		# On remet le tab global
		self.init_tab_global()
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
		self.CTRL.launch_simulation(self, self.activ_sim)

	#############################################

	def update_head(self):
		# Méthode pour update l'interface
		self.labelmeteo.setText(f"Meteo: {self.CTRL.get_meteo(self.activ_sim)}")
		self.labelday.setText(f"Days: {self.CTRL.get_day(self.activ_sim)}")
		self.labelhour.setText(f"hour: {self.CTRL.get_hour(self.activ_sim)}")
		self.labelnbrover.setText(f"nb Rover: {self.CTRL.get_nbrover(self.activ_sim)}")


	def update_graph(self):
		# Méthode pour update les graphes
		print("On update les graph")
		time = self.CTRL.get_time(self.activ_sim)
		# On se balade dans la liste des tab des rovers
		for x in range(len(self.lstabrover)):
			print("les graphes des rovers")
			self.lstabrover[x].widget(1).update_components(self.CTRL.get_components_durability_all(self.activ_sim,x), time)
		# On update pour le global
		# On recup le widget
		global_tab = self.tab.widget(0)
		# Meteo
		global_tab.widget(1).update_meteo(time, self.CTRL.get_meteo(self.activ_sim))
		# Température
		global_tab.widget(2).update_temp(time, self.CTRL.get_temp(self.activ_sim))
		# NbRover fonctionnel
		global_tab.widget(3).update_rover(time, self.CTRL.get_alive_rover(self.activ_sim))

	def update_load(self):
		# Méthode pour Recharger l'interface après le load d'une save
		# On update l'entête
		self.update_head()
		# On update les tableaux
		# On reset les log
		self.reset_log()
		# On reset le tableau des rover
		self.reset_tabrover()
		# On remet le tab global
		self.init_tab_global()
		# On remet les tableaux des rover
		for x in range(self.CTRL.get_nbrover(self.activ_sim)):
			# On ajoute un nouveau string à remplir
			self.tabstringrover += [""]
			# On appel l'ajout d'un nouveau tab rover
			self.add_tab_rover()
			# On appel l'ajout de label rover
			self.add_label_rover()
			# On appel l'ajout de graph des rovers
			self.add_graphe_rover(len(self.lslabelrover)-1, "components")
			# On load les données des tableaux du Rover
			# TO DO
			# Charger les logs de chaque rover
			rover_log = self.CTRL.get_simulation(self.activ_sim).get_rover_log()
			self.tabstringrover[x] = rover_log
			self.lslabelrover[x].setText(rover_log)
			
			# Charger les graphes pour ce rover
			components_data = self.CTRL.get_components_durability_all(self.activ_sim, x)
			self.lstabrover[x].widget(1).update_components(components_data, self.CTRL.get_time(self.activ_sim))

		# On charge les données des tableaux Globaux
		time = self.CTRL.get_time(self.activ_sim)
		# On load les données des tableaux Globaux
		# TO DO
		# Update global graphs
		global_tab = self.tab.widget(0)
		global_tab.widget(1).update_meteo(time, self.CTRL.get_meteo(self.activ_sim))
		global_tab.widget(2).update_temp(time, self.CTRL.get_temp(self.activ_sim))
		global_tab.widget(3).update_rover(time, self.CTRL.get_alive_rover(self.activ_sim))

	##### Menu Button ####
	def back_button(self):
		# Méthode pour gérer l'action du boutton save menu
		self.CTRL.back_menu()

	def button_stop(self):
		# Méthode pour créer un button pour mettre en pause l'éxécution de la Simulation
		button = QPushButton("Stop")
		button.clicked.connect(self.button_stop_clicked)
		self.layoutbutton.addWidget(button)

	def button_stop_clicked(self):
		# Méthode pour arrêter l'éxécutions de la simulation
		self.CTRL.stop_simulation()



	##### Dialogue Simulation ####
	def dialog_simulation(self, main_window, save = 0):
		# Méthode pour créer et afficher la window de chargement de simulation
		# Même Interface entre Save et load outre le titre et l'action
		dlg = QDialog(main_window)
		if save == 0:
			dlg.setWindowTitle("Load simulation")
		else:
			dlg.setWindowTitle("Save simulation")

		#### Set Layout ####
		global_layout = QVBoxLayout()
		button_layout = QHBoxLayout()

		Qlist = QListWidget()
		self.dialog_init_list(Qlist)
		global_layout.addWidget(Qlist)
		global_layout.addLayout(button_layout)

		#### Set Button ####
		# Open
		if(save == 0):
			button = QPushButton("Open")
			button.clicked.connect(lambda: self.dialog_load(dlg, Qlist))
		else:
			# Boutton pour créer un nouveaux
			button_create = QPushButton("New")
			button_create.clicked.connect(lambda: self.dialog_new(dlg,Qlist))
			button_layout.addWidget(button_create)
			# Boutton pour sauvegarder
			button = QPushButton("Save")
			button.clicked.connect(lambda: self.dialog_save(dlg, Qlist))
		button_layout.addWidget(button)
		# Cancel
		button = QPushButton("Cancel")
		button.clicked.connect(lambda: self.dialog_exit(dlg))
		button_layout.addWidget(button)


		dlg.setLayout(global_layout)
		dlg.exec()

	def dialog_init_list(self, Qlist):
		# Méthode liées au dialogue load simulation
		# On recup la liste des fichiers dans le dossiers des simulation
		ls_file = scan_simulation_file()
		# On créer la liste
		Qlist.addItems(ls_file)


	def dialog_load(self, dlg, Qlist):
		# Méthode liées au button load du dialog load simulation
		print("objet actuelle:", Qlist.currentItem().text())
		# On recup le nom
		filename = Qlist.currentItem().text()
		# On le balance au Controler
		self.CTRL.load_simulation(self.activ_sim, filename) 

		# On update l'interface/Reload
		self.update_load()
		# On ferme la fenêtre
		dlg.close()

	def dialog_save(self, dlg, Qlist):
		# Méthode liées au button load du dialog load simulation
		print("objet actuelle:", Qlist.currentItem().text())
		# On recup le nom
		filename = Qlist.currentItem().text()
		# On le balance au Controler
		self.CTRL.save_simulation(self.activ_sim,filename)
		# On ferme la fenêtre
		dlg.close()

	def dialog_new(self, dlg, Qlist):
		# Méthode liées à la création d'une nouvelle sauvegade
		# On créer un nouveaux Dialogue
		dlg2 = QDialog(dlg)
		dlg2.setWindowTitle("New Save Name")
		# On met en place le layout
		layout_global = QVBoxLayout()
		layout_button = QHBoxLayout()
		# On met le line edit pour entréer la nouvelle sauvegarde
		line_edit = QLineEdit()
		layout_global.addWidget(line_edit)
		# On met en place le boutton Back
		button = QPushButton("Back")
		button.clicked.connect(lambda: self.dialog_exit(dlg2))
		layout_button.addWidget(button)
		# On met en place le boutton OK
		button = QPushButton("Save")
		button.clicked.connect(lambda: self.dialog_new_save(dlg2,Qlist, line_edit))
		layout_button.addWidget(button)

		# On set au layout
		layout_global.addLayout(layout_button)
		dlg2.setLayout(layout_global)
		dlg2.exec()


	def dialog_new_save(self, dlg, Qlist, line_edit):
		# Méthode pour vérifier le nom est lancer la sauvegarde
		# On récup le txt
		txt = line_edit.text()
		# On appel la méthode du CTRL
		self.CTRL.save_simulation(self.activ_sim,txt)
		# On update la liste des Save
		Qlist.addItems([txt])
		# On ferme la fenêtre
		dlg.close()


	def dialog_exit(self, dlg):
		# Méthode liées au button exit du dialog load simulation
		dlg.close()
