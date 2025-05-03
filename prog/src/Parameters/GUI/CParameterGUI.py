########################################################################
# Fichier qui vient Contenir la Parameter GUI
# Initialiser dans Users
########################################################################


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTabWidget, QScrollArea, QLineEdit, QDialog, QListWidget

from src.Parameters.Controler.CParameterCTRL import CParameterCTRL
from src.Simulation.CData import scan_parameter_file

class CParameterGUI(QWidget):
	def __init__(self, main_window, sim_factory, param_factory):
		# On initialise la classe hérité
		super().__init__()

		self.activ_param = 0
		# On link le CTRL
		self.CTRL = CParameterCTRL(main_window, sim_factory, param_factory)

		# On initialise un Paramètre
		self.CTRL.create_parameter()


		self.ls_line = []
		# On setup le layout
		self.init_layout(main_window)


	##### Initialisation Layout #####

	def init_layout(self, main_window):
		# Méthode pour initialiser le layout

		self.layout = QVBoxLayout()
		# Initialise le layout Paramètre
		self.init_parameter()

		self.layoutbutton = QHBoxLayout()
		# Initialise le layout Button
		self.init_button(main_window)
		self.layout.addLayout(self.layoutbutton)

		self.setLayout(self.layout)


	#### Initialise les Bouttons ####
	def init_button(self, main_window):
		# Méthode pour initiliser l'affichage des bouttons


		subleft_layoutbutton = QVBoxLayout()
		subcenter_layoutbutton = QVBoxLayout()

		# Centre
		# Boutton lancement de parameter
		button = QPushButton("Launch Simulation")
		button.clicked.connect(self.launch_sim_clicked)
		subcenter_layoutbutton.addWidget(button)
		# Boutton back
		button = QPushButton("Back")
		button.clicked.connect(self.back_clicked)
		subcenter_layoutbutton.addWidget(button)

		# gauche

		# Boutton Save Preset
		button = QPushButton("Save Preset")
		button.clicked.connect(lambda: self.save_preset_clicked(main_window))
		subleft_layoutbutton.addWidget(button, alignment = Qt.AlignmentFlag.AlignLeft)

		# Boutton Load Preset
		button = QPushButton("Load Preset")
		button.clicked.connect(lambda: self.load_preset_clicked(main_window))
		subleft_layoutbutton.addWidget(button, alignment = Qt.AlignmentFlag.AlignLeft)

		self.layoutbutton.addLayout(subleft_layoutbutton)
		self.layoutbutton.addLayout(subcenter_layoutbutton)


	#### Initialise l'affichage des paramètre ####

	def init_parameter(self):
		# Méthode pour initialiser l'affichage des label param avec QLineEdit

		self.layoutParameter = QVBoxLayout()
		self.layout.addLayout(self.layoutParameter)

		# MaxDays

		layout_days = QHBoxLayout()
		label_text = QLabel("Durée de la parameter: ")
		layout_days.addWidget(label_text)

		line_edit = QLineEdit(str(self.CTRL.get_maxdays(self.activ_param)))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_maxdays(s))
		layout_days.addWidget(line_edit)
		self.ls_line += [line_edit]

		self.layoutParameter.addLayout(layout_days)

		# Météo

		# SandStorm Storm
		label_text = QLabel("Tempête de Sable:")
		self.layoutParameter.addWidget(label_text)

		layout_sandstorm = QHBoxLayout()

		label_text = QLabel("Probabilité d'Apparition: ")
		layout_sandstorm.addWidget(label_text)

		line_edit = QLineEdit(str(self.CTRL.get_sandstorm_probability_spawn(self.activ_param)))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_sandstorm_probability_spawn(s))
		# lambda s: self.setmaxdays(s)
		layout_sandstorm.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Probabilité de Disparition: ")
		layout_sandstorm.addWidget(label_text)

		line_edit = QLineEdit(str(self.CTRL.get_sandstorm_probability_despawn(self.activ_param)))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_sandstorm_probability_despawn(s))
		# lambda s: self.setmaxdays(s)
		layout_sandstorm.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Dégats")
		layout_sandstorm.addWidget(label_text)

		line_edit = QLineEdit(str(self.CTRL.get_sandstorm_damage(self.activ_param)))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_sandstorm_damage(s))
		# lambda s: self.setmaxdays(s)
		layout_sandstorm.addWidget(line_edit)
		self.ls_line += [line_edit]


		self.layoutParameter.addLayout(layout_sandstorm)


		# Solar Storm
		label_text = QLabel("Tempête Solaire:")
		self.layoutParameter.addWidget(label_text)
		layout_solarstorm = QHBoxLayout()

		label_text = QLabel("Probabilité d'Apparition: ")
		layout_solarstorm.addWidget(label_text)

		line_edit = QLineEdit(str(self.CTRL.get_solarstorm_probability_spawn(self.activ_param)))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_solarstorm_probability_spawn(s))
		# lambda s: self.setmaxdays(s)
		layout_solarstorm.addWidget(line_edit)
		self.ls_line += [line_edit]


		label_text = QLabel("Probabilité de Disparition: ")
		layout_solarstorm.addWidget(label_text)

		line_edit = QLineEdit(str(self.CTRL.get_solarstorm_probability_despawn(self.activ_param)))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_solarstorm_probability_despawn(s))
		# lambda s: self.setmaxdays(s)
		layout_solarstorm.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Dégats")
		layout_solarstorm.addWidget(label_text)

		line_edit = QLineEdit(str(self.CTRL.get_solarstorm_damage(self.activ_param)))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_solarstorm_damage(s))
		# lambda s: self.setmaxdays(s)
		layout_solarstorm.addWidget(line_edit)
		self.ls_line += [line_edit]


		self.layoutParameter.addLayout(layout_solarstorm)

		# Composants

		label_text = QLabel("Composants Rover:")
		self.layoutParameter.addWidget(label_text)

		#### Roue ####
		label_text = QLabel("Roue:")
		self.layoutParameter.addWidget(label_text)


		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)

		line_edit = QLineEdit(str(self.CTRL.get_components_durability(self.activ_param, "wheel")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("Wheel", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]


		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_resistance(self.activ_param, "wheel")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("Wheel", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]


		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_damage(self.activ_param, "wheel")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("Wheel", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]


		self.layoutParameter.addLayout(layout_components)

		#### Bras ####
		label_text = QLabel("Bras:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_durability(self.activ_param,"arm")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("arm", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_resistance(self.activ_param, "arm")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("arm", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]


		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_damage(self.activ_param,"arm")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("arm", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		self.layoutParameter.addLayout(layout_components)

		#### Chassis ####
		label_text = QLabel("Chassis:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_durability(self.activ_param,"frame")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("frame", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_resistance(self.activ_param,"frame")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("frame", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_damage(self.activ_param,"frame")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("frame", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		self.layoutParameter.addLayout(layout_components)

		##### Caméra ####
		label_text = QLabel("Caméra:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_durability(self.activ_param,"camera")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("camera", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_resistance(self.activ_param,"camera")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("camera", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_damage(self.activ_param,"camera")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("camera", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		self.layoutParameter.addLayout(layout_components)

		#### Panneaux Solaire ####
		label_text = QLabel("Panneaux Solaire:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_durability(self.activ_param,"solar_panel")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("solar_panel", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_resistance(self.activ_param,"solar_panel")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("solar_panel", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]


		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_damage(self.activ_param,"solar_panel")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("solar_panel", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		self.layoutParameter.addLayout(layout_components)

		#### Batterie ####
		label_text = QLabel("Batterie:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_durability(self.activ_param,"cell")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("cell", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_resistance(self.activ_param,"cell")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("cell", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]


		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_damage(self.activ_param,"cell")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("cell", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		self.layoutParameter.addLayout(layout_components)

		##### Antenne ####
		label_text = QLabel("Antenne:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_durability(self.activ_param,"antenna")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("antenna", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(self.CTRL.get_components_resistance(self.activ_param,"antenna")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("antenna", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)

		line_edit = QLineEdit(str(self.CTRL.get_components_damage(self.activ_param,"antenna")))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("antenna", s))
		layout_components.addWidget(line_edit)
		self.ls_line += [line_edit]

		self.layoutParameter.addLayout(layout_components)


	#### Initialisation label text ####

	def init_label_text(self):
		# Méthode pour initialiser label text
		pass

	#### Initialisation QLineEdit ####
	def init_line_edit(self):
		# Méthode pour initialiser line edit
		pass



	#### Line Edit ####

	def set_maxdays(self, line_edit):
		# Méthode liée au Line Edit de Maxdays
		s = line_edit.text()
		print("Change Maxdays s:",s)
		if s.isnumeric():
			self.CTRL.set_maxdays(self.activ_param, int(s))


	# Météo
	# Sandstorm
	def set_sandstorm_probability_spawn(self, line_edit):
		# Méthode pour set la probabilité de spawn d'une tempête de sable
		s = line_edit.text()
		print("Change sandstorm probability spawn s:",s)
		if s.isnumeric():
			self.CTRL.set_sandstorm_probability_spawn(self.activ_param, int(s))

	def set_sandstorm_probability_despawn(self, line_edit):
		# Méthode pour set la probabilité de despawn d'une tempête de sable
		s = line_edit.text()
		print("Change sandstorm probability despawn s:",s)
		if s.isnumeric():
			self.CTRL.set_sandstorm_probability_despawn(self.activ_param, int(s))

	def set_sandstorm_damage(self, line_edit):
		# méthode pour set les dégâts d'une tempête de sable
		s = line_edit.text()
		print("Change sandstorm damage s:",s)
		if s.isnumeric():
			self.CTRL.set_sandstorm_damage(self.activ_param, int(s))

	# SolarSorm
	def set_solarstorm_probability_spawn(self, line_edit):
		# Méthode pour set la probabilité de spawn d'une tempête de sable
		s = line_edit.text()
		print("Change solarstorm probability spawn s:",s)
		if s.isnumeric():
			self.CTRL.set_solarstorm_probability_spawn(self.activ_param, int(s))

	def set_solarstorm_probability_despawn(self, line_edit):
		# Méthode pour set la probabilité de despawn d'une tempête de sable
		s = line_edit.text()
		print("Change solarstorm probability despawn s:",s)
		if s.isnumeric():
			self.CTRL.set_solarstorm_probability_despawn(self.activ_param, int(s))

	def set_solarstorm_damage(self, line_edit):
		# méthode pour set les dégâts d'une tempête de sable
		s = line_edit.text()
		print("Change solarstorm damage s:",s)
		if s.isnumeric():
			self.CTRL.set_solarstorm_probability_damage(self.activ_param, int(s))

	# Température
	def set_maxtemp(self, line_edit):
		# Méthode pour set la température max
		s = line_edit.text()
		print("Change maxtemp s:",s)
		if s.isnumeric():
			self.CTRL.set_maxtemp(self.activ_param, int(s))

	def set_mintemp(self, line_edit):
		# Méthode pour set la température min
		s = line_edit.text()
		print("Change mintemp s:",s)
		if s.isnumeric():
			self.CTRL.set_mintemp(self.activ_param, int(s))

	# Composants

	def set_components_durability(self, components, line_edit):
		# Méthode pour set la durabilité d'un composants
		s = line_edit.text()
		print("Change durability components, s:", components, s)
		if s.isnumeric():
			self.CTRL.set_components_durability(self.activ_param, components, int(s))

	def set_components_resistance(self, components, line_edit):
		# Méthode pour set la résistance d'un composants
		s = line_edit.text()
		print("Change resistance components, s:",components, s)
		if s.isnumeric():
			self.CTRL.set_components_resistance(self.activ_param, components, int(s))

	def set_components_damage(self, components, line_edit):
		# Méthode pour set les dégâts du composants pris par tour
		s = line_edit.text()
		print("Change damage components, s:",components,s)
		if s.isnumeric():
			self.CTRL.set_components_damage(self.activ_param, components, int(s))


	#### Button ####
	def launch_sim_clicked(self):
		# Méthode pour gérer l'event clicked sur le bouton launch SIm
		self.CTRL.launch_sim(self.activ_param)

	def back_clicked(self):
		# Méthode pour gérer l'event clicked sur le bouton back
		self.CTRL.back()


	def save_preset_clicked(self, main_window):
		# Méthode pour gérer l'event clicked sur le bouton save preset
		# On affiche Un Line edit Ou on demande d'entrée le nom du fichier
		self.dialog_parameter(main_window, 1)

	def load_preset_clicked(self, main_window):
		# Méthode pour gérer l'event clicked sur le bouton load preset
		# On affiche une interface afin de sélectioner l'un des fichiers trouvées
		self.dialog_parameter(main_window)


	##### Dialogue Preset Parameter ####
	def dialog_parameter(self, main_window, save = 0):
		# Méthode pour créer et afficher la window de chargement de parameter
		# Même Interface entre Save et load outre le titre et l'action
		dlg = QDialog(main_window)
		if save == 0:
			dlg.setWindowTitle("Load Parameter")
		else:
			dlg.setWindowTitle("Save Parameter")

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
		# Méthode liées au dialogue load parameter
		# On recup la liste des fichiers dans le dossiers des parameter
		ls_file = scan_parameter_file()
		# On créer la liste
		Qlist.addItems(ls_file)


	def dialog_load(self, dlg, Qlist):
		# Méthode liées au button load du dialog load Parameter
		print("objet actuelle:", Qlist.currentItem().text())
		# On recup le nom
		filename = Qlist.currentItem().text()
		# On le balance au Controler
		self.CTRL.load_preset(self.activ_param,filename)
		# On update l'interface
		self.update_line()
		# On ferme la fenêtre
		dlg.close()

	def dialog_save(self, dlg, Qlist):
		# Méthode liées au button load du dialog load Parameter
		print("objet actuelle:", Qlist.currentItem().text())
		# On recup le nom
		filename = Qlist.currentItem().text()
		# On le balance au Controler
		self.CTRL.save_preset(self.activ_param,filename)
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
		self.CTRL.save_preset(self.activ_param,txt)
		# On update la liste des Save
		Qlist.addItem(txt)
		# On ferme la fenêtre
		dlg.close()


	def dialog_exit(self, dlg):
		# Méthode liées au button exit du dialog load parameter
		dlg.close()

	def update_line(self):
		# Méthode pour update les lines après load parameter
		#Maxdays
		self.ls_line[0].setText(str(self.CTRL.get_maxdays(self.activ_param)))
		#SandStorm Spawn
		self.ls_line[1].setText(str(self.CTRL.get_sandstorm_probability_spawn(self.activ_param)))
		#SandStorm Despawn
		self.ls_line[2].setText(str(self.CTRL.get_sandstorm_probability_despawn(self.activ_param)))
		#SandStorm Damage
		self.ls_line[3].setText(str(self.CTRL.get_sandstorm_damage(self.activ_param)))

		#SolarStorm Spawn
		self.ls_line[4].setText(str(self.CTRL.get_solarstorm_probability_spawn(self.activ_param)))
		#SolarStorm Despawn
		self.ls_line[5].setText(str(self.CTRL.get_solarstorm_probability_despawn(self.activ_param)))
		#SolarStorm Damage
		self.ls_line[6].setText(str(self.CTRL.get_solarstorm_damage(self.activ_param)))
		i = 7
		#Component
		for components in ["wheel","arm","frame","camera","solar_panel","cell","antenna"]:
			self.ls_line[i].setText(str(self.CTRL.get_components_durability(self.activ_param, components)))
			self.ls_line[i+1].setText(str(self.CTRL.get_components_resistance(self.activ_param, components)))
			self.ls_line[i+2].setText(str(self.CTRL.get_components_damage(self.activ_param, components)))
			i += 3


