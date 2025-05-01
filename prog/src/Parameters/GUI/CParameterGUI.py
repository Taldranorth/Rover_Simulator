########################################################################
# Fichier qui vient Contenir la Parameter GUI
# Initialiser dans Users
########################################################################

from src.Parameters.Controler.CParameterCTRL import CParameterCTRL

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTabWidget, QScrollArea, QLineEdit


class CParameterGUI(QWidget):
	def __init__(self, main_window, param_factory):
		# On initialise la classe hérité
		super().__init__()

		self.activ_param = 0
		# On link le CTRL
		self.CTRL = CParameterCTRL(main_window, param_factory)

		# On initialise un Paramètre
		self.CTRL.create_parameter()

		# On setup le layout
		self.init_layout()


	##### Initialisation Layout #####

	def init_layout(self):
		# Méthode pour initialiser le layout

		self.layout = QVBoxLayout()
		# Initialise le layout Paramètre
		self.init_parameter()

		self.layoutbutton = QHBoxLayout()
		# Initialise le layout Button
		self.init_button()
		self.layout.addLayout(self.layoutbutton)

		self.setLayout(self.layout)


	#### Initialise les Bouttons ####
	def init_button(self):
		# Méthode pour initiliser l'affichage des bouttons


		subleft_layoutbutton = QVBoxLayout()
		subcenter_layoutbutton = QVBoxLayout()

		# Centre
		# Boutton lancement de Simulation
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
		button.clicked.connect(self.save_preset_clicked)
		subleft_layoutbutton.addWidget(button)

		# Boutton Load Preset
		button = QPushButton("Load Preset")
		button.clicked.connect(self.load_preset_clicked)
		subleft_layoutbutton.addWidget(button)

		self.layoutbutton.addLayout(subleft_layoutbutton)
		self.layoutbutton.addLayout(subcenter_layoutbutton)


	#### Initialise l'affichage des paramètre ####

	def init_parameter(self):
		# Méthode pour initialiser l'affichage des label param avec QLineEdit

		parameter = self.CTRL.get_parameter(self.activ_param)

		self.layoutParameter = QVBoxLayout()
		self.layout.addLayout(self.layoutParameter)

		# MaxDays

		layout_days = QHBoxLayout()
		label_text = QLabel("Durée de la Simulation: ")
		layout_days.addWidget(label_text)

		line_edit = QLineEdit(str(parameter.maxdays))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_maxdays(s))
		# lambda s: self.setmaxdays(s)
		layout_days.addWidget(line_edit)

		self.layoutParameter.addLayout(layout_days)

		# Météo

		# SandStorm Storm
		label_text = QLabel("Tempête de Sable:")
		self.layoutParameter.addWidget(label_text)

		layout_sandstorm = QHBoxLayout()

		label_text = QLabel("Probabilité d'Apparition: ")
		layout_sandstorm.addWidget(label_text)

		line_edit = QLineEdit(str(parameter.sandstorm_probability_spawn))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_sandstorm_probability_spawn(s))
		# lambda s: self.setmaxdays(s)
		layout_sandstorm.addWidget(line_edit)

		label_text = QLabel("Probabilité de Disparition: ")
		layout_sandstorm.addWidget(label_text)

		line_edit = QLineEdit(str(parameter.sandstorm_probability_despawn))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_sandstorm_probability_despawn(s))
		# lambda s: self.setmaxdays(s)
		layout_sandstorm.addWidget(line_edit)

		label_text = QLabel("Dégats")
		layout_sandstorm.addWidget(label_text)

		line_edit = QLineEdit(str(parameter.sandstorm_damage))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_sandstorm_damage(s))
		# lambda s: self.setmaxdays(s)
		layout_sandstorm.addWidget(line_edit)


		self.layoutParameter.addLayout(layout_sandstorm)


		# Solar Storm
		label_text = QLabel("Tempête Solaire:")
		self.layoutParameter.addWidget(label_text)
		layout_solarstorm = QHBoxLayout()

		label_text = QLabel("Probabilité d'Apparition: ")
		layout_solarstorm.addWidget(label_text)

		line_edit = QLineEdit(str(parameter.solarstorm_probability_spawn))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_solarstorm_probability_spawn(s))
		# lambda s: self.setmaxdays(s)
		layout_solarstorm.addWidget(line_edit)


		label_text = QLabel("Probabilité de Disparition: ")
		layout_solarstorm.addWidget(label_text)

		line_edit = QLineEdit(str(parameter.solarstorm_probability_despawn))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_solarstorm_probability_despawn(s))
		# lambda s: self.setmaxdays(s)
		layout_solarstorm.addWidget(line_edit)

		label_text = QLabel("Dégats")
		layout_solarstorm.addWidget(label_text)

		line_edit = QLineEdit(str(parameter.solarstorm_damage))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_solarstorm_damage(s))
		# lambda s: self.setmaxdays(s)
		layout_solarstorm.addWidget(line_edit)


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

		line_edit = QLineEdit(str(parameter.wheel_durability))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("Wheel", s))
		layout_components.addWidget(line_edit)


		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.wheel_rs))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("Wheel", s))
		layout_components.addWidget(line_edit)


		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.wheel_damage))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("Wheel", s))
		layout_components.addWidget(line_edit)


		self.layoutParameter.addLayout(layout_components)

		#### Bras ####
		label_text = QLabel("Bras:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.arm_durability))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("arm", s))
		layout_components.addWidget(line_edit)

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.arm_rs))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("arm", s))
		layout_components.addWidget(line_edit)


		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.arm_damage))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("arm", s))
		layout_components.addWidget(line_edit)

		self.layoutParameter.addLayout(layout_components)

		#### Chassis ####
		label_text = QLabel("Chassis:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.frame_durability))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("frame", s))
		layout_components.addWidget(line_edit)

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.frame_rs))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("frame", s))
		layout_components.addWidget(line_edit)

		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.frame_damage))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("frame", s))
		layout_components.addWidget(line_edit)

		self.layoutParameter.addLayout(layout_components)

		##### Caméra ####
		label_text = QLabel("Caméra:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.camera_durability))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("camera", s))
		layout_components.addWidget(line_edit)

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.camera_rs))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("camera", s))
		layout_components.addWidget(line_edit)

		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.camera_damage))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("camera", s))
		layout_components.addWidget(line_edit)

		self.layoutParameter.addLayout(layout_components)

		#### Panneaux Solaire ####
		label_text = QLabel("Panneaux Solaire:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.solar_panel_durability))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("solar_panel", s))
		layout_components.addWidget(line_edit)

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.solar_panel_rs))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("solar_panel", s))
		layout_components.addWidget(line_edit)


		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.solar_panel_damage))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("solar_panel", s))
		layout_components.addWidget(line_edit)

		self.layoutParameter.addLayout(layout_components)

		#### Batterie ####
		label_text = QLabel("Batterie:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.cell_durability))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("cell", s))
		layout_components.addWidget(line_edit)

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.cell_rs))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("cell", s))
		layout_components.addWidget(line_edit)


		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.cell_damage))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("cell", s))
		layout_components.addWidget(line_edit)

		self.layoutParameter.addLayout(layout_components)

		##### Antenne ####
		label_text = QLabel("Antenne:")
		self.layoutParameter.addWidget(label_text)

		layout_components = QHBoxLayout()
		label_text = QLabel("Durabilité: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.antenna_durability))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_durability("antenna", s))
		layout_components.addWidget(line_edit)

		label_text = QLabel("Résistance: ")
		layout_components.addWidget(label_text)
		line_edit = QLineEdit(str(parameter.antenna_rs))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_resistance("antenna", s))
		layout_components.addWidget(line_edit)

		label_text = QLabel("Dégats: ")
		layout_components.addWidget(label_text)

		line_edit = QLineEdit(str(parameter.maxdays))
		line_edit = QLineEdit(str(parameter.antenna_damage))
		line_edit.returnPressed.connect(lambda s = line_edit: self.set_components_damage("antenna", s))
		layout_components.addWidget(line_edit)

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
		pass

	def back_clicked(self):
		# Méthode pour gérer l'event clicked sur le bouton back
		pass



	def save_preset_clicked(self):
		# Méthode pour gérer l'event clicked sur le bouton save preset
		pass

	def load_preset_clicked(self):
		# Méthode pour gérer l'event clicked sur le bouton load preset
		pass


