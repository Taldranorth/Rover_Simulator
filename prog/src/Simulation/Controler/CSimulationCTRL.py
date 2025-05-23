########################################################################
# Fichier qui vient Contenir la Classe Controller de la Simulation
# Initialiser dans Users
########################################################################

from threading import Thread
from time import sleep


class CSimulationCTRL:
	def __init__(self, main_window, sim_factory, param_factory):
		# link vers la window
		self.main_window = main_window
		# On set les factory
		self.sim_factory = sim_factory
		self.param_factory = param_factory

		# Pour les Thread
		self.stop = False

	# Setter
	# Simulation
	def create_simulation(self, CParam):
		# Méthode pour ajouter une simulation par la méthode de la factory
		self.sim_factory.create_simulation(CParam)

	def remove_simulation(self, i):
		# Méthode pour retirer une simulation
		self.sim_factory.remove_simulation(i)

	def get_simulation(self, i):
		# Méthode pour récupérer l'objet SImulation à la I place
		return self.sim_factory.get_simulation(i)

	def create_Rover(self, i):
		# Méthode pour appeler la création d'un rover dans I ième simulation de la liste
		self.sim_factory.create_Rover(i)


	# Parameter

	def create_parameter(self):
		# Méthode pour ajouter une simulation par la méthode de la factory
		self.param_factory.create_parameter()

	def remove_parameter(self, i):
		# Méthode pour retirer une simulation
		self.param_factory.remove_parameter(i)

	def get_parameter(self, i):
		# Méthode pour récupérer l'objet parameter à la I place
		return self.param_factory.get_parameter(i)

	##### Button #####

	def reset_simulation(self, i):
		# Méthode pour reset la Simulation

		# On supprime la simulation
		self.remove_simulation(i)
		# On recréer la simulation
		self.create_simulation(self.get_parameter(i))


	#### Gestion Loop ####

	def update_loop(self, GUI, i):
		# Méthode pour update la loop et renvoyer les données au GUI
		s = self.get_simulation(i)
		time = s.delays
		while((s.is_end() == False) and (self.stop == False)):
			# On sleep
			#sleep(i)
			# On update
			s.update_hour()
			# On affiche dans le terminal
			s.afficher()
			# On redirige vers le Window text
			GUI.add_log(self.get_rover_log(i))
			for x in range(self.get_nbrover(i)):
				GUI.add_log_rover(self.get_single_rover_log(i,x),x)
			# On update les graphes
			GUI.update_graph()
			# On update l'header
			GUI.update_head()
			# On dit à l'appli d'update l'affichage
			self.main_window.app.processEvents()
			sleep(i)
			# On programme la prochaine executions du programme
			#next_thread = Thread(target = self.update_loop(GUI, i))
			#next_thread.start()
			#Thread.exit()


	def stop_simulation(self):
		# Méthode pour mettre en pause l'éxécutions de la simulation
		self.stop = True

	def launch_simulation(self, GUI, i):
		# Méthode pour lancer l'éxécutions de la simulation
		self.stop = False
		self.update_loop(GUI, i)

	#############################################


	def save_simulation(self, i, filename):
		# Méthode pour gérer la sauvegarde de la Simulation
		self.sim_factory.save_simulation(i, filename)


	def load_simulation(self, i, filename):
		# Méthode pour gérer le chargement de la Simulation
		self.sim_factory.load_simulation(i, filename)


	def back_menu(self):
		# Méthode pour gérer le retour au Menu Principale
		self.main_window.change_GUI("CMenuGUI")


	def get_rover_log(self, isim):
		return self.sim_factory.get_rover_log(isim)

	def get_single_rover_log(self, isim, irover):
		# Méthode pour récupérer le log du rover
		return self.sim_factory.get_single_rover_log(isim, irover)

	def get_meteo(self, i):
		# Méthode pour récup la météo
		return self.sim_factory.get_meteo(i)

	def get_day(self, i):
		# Méthode pour récup le jour
		return self.sim_factory.get_day(i)

	def get_hour(self, i):
		# Méthode pour récup l'heure
		return self.sim_factory.get_hour(i)

	def get_nbrover(self, i):
		# Méthode pour récupérer le nombre de rover
		return self.sim_factory.get_nbrover(i)

	def get_alive_rover(self, i):
		# Méthode pour récupérer le nb de rover en état de marche
		return self.sim_factory.get_alive_rover(i)

	def get_temp(self, i):
		# Méthode pour récupérer la temp de la simulation
		return self.sim_factory.get_temp(i)

	def get_time(self, i):
		# Méthode qui retourne le temp (jour + heure)
		day = self.sim_factory.get_day(i)
		hour = self.sim_factory.get_hour(i)

		return (day+(hour/100))

	def get_components_durability_all(self,isim,irover):
		# Méthode qui retourne la durabilités du tout les composants du rover
		return self.sim_factory.get_components_durability_all(isim,irover)


	def get_time_data(self, isim):
		# Méthode qui retourne la liste xdata nécessaire pour l'abcisse des graphes aux chargement
		ls = []
		day = 0
		daymax = self.sim_factory.get_day(isim)
		hour = 0
		hourmax = self.sim_factory.get_hour(isim)

		while(day < daymax):
			hour += 1
			if hour == 24:
				hour = 0
				day += 1
			ls += [day+(hour/100)]
		hour = 0
		while hour < hourmax:
			ls += [day+(hour/100)]
			hour += 1
		return ls

	def get_components_data(self, isim, irover):
		# Méthode qui retourne la liste ydata nécessaire pour l'ordonnées des graphes aux chargement
		ls = [[],[],[],[],[],[],[]]
		data = self.sim_factory.get_history_rover(isim, irover)
		i = 0
		for string in ["wheel1","arm","frame","camera","solar_pannel","cell","antenna"]:
			ls[i] = data[string]
			i += 1
		return ls

	def get_meteo_data(self, isim):
		# Méthode qui retourne la liste ydata nécessaire pour l'ordonnées des graphes aux chargement
		data = self.sim_factory.get_history_simulation(isim)
		ls = [[],[],[]]
		for x in range(len(data["meteo"])):
			meteo = data["meteo"][x]
			if meteo == "SandStorm":
				ls[0] += [1]
				ls[1] += [0]
				ls[2] += [0]
			elif meteo == "SolarStorm":
				ls[0] += [0]
				ls[1] += [1]
				ls[2] += [0]
			else:
				ls[0] += [0]
				ls[1] += [0]
				ls[2] += [1]				
		return ls


	def get_temperature_data(self, isim):
		# Méthode qui retourne la liste ydata nécessaire pour l'ordonnées des graphes aux chargement
		data = self.sim_factory.get_history_simulation(isim)
		ls = data["temperature"]
		return ls


	def get_rover_data(self, isim):
		# Méthode qui retourne la liste ydata nécessaire pour l'ordonnées des graphes aux chargement
		data = self.sim_factory.get_history_simulation(isim)
		ls = data["roveralive"]
		return ls





