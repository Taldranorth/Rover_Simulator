#######
# Fichier Principal
#######
import sys
import PyQt6

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QSlider, QHBoxLayout, QScrollArea

from queue import Queue 
from threading import Thread 

# Import factory
from src.Parameters.factory.CParameterFactory import CParameterFactory
from src.Simulation.factory.CSimulationFactory import CSimulationFactory

# Import GUI
from src.Menu.CMenuGUI import CMenuGUI
from src.Simulation.GUI.CSimulationGUI import CSimulationGUI
from src.Parameters.GUI.CParameterGUI import CParameterGUI
from src.Authentification.GUI.LoginGui import CLoginGUI
# Import DB
from src.Authentification.DAO.UserDao import init_db

# Rappel:
# - GUI = interface graphique
# - Controler = controler de l'interface GUI (appeler les setter) NE MODIFIE PAS DIRECTEMENT LES DONNÉES
# - DAO = Data Access Object, transfert des données de la base de données en données utilisable en programme


class CMainWindow(QMainWindow):
    def __init__(self, app):
        # Initialiser la classe hérité
        super().__init__()
        # Attribut Application 
        self.app = app
        # Initialise le titre
        self.setWindowTitle("Rover Simulator")
        # On garde une référence au widget actuellement actif
        widget = 0
        # On déplace la fenêtre en haut à gauche
        self.move(0,0)

        # On link les singletons Factory
        self.sim_factory = 0
        self.param_factory = 0
        self.user_factory = 0

        # Pour indiquer si il y a un serveur Connecté
        self.server = 0

        # On veut que la fenêtre soit montré
        self.show()

    # Setter
    def set_window_size(self, Width, Height):
        # Méthode pour set la hauteur et la largeur de la window
        self.setFixedSize(Width, Height)

    def set_sim_factory(self, sim_factory):
        # Méthode pour set la Simulation Factory
        self.sim_factory = sim_factory

    def set_param_factory(self, param_factory):
        # Méthode pour set la Paramètre Factory
        self.param_factory = param_factory

    def set_user_factory(self, user_factory):
        # Méthode pour set le User Factory
        self.user_factory = user_factory

    def change_GUI(self, GUI):
        # Méthode pour changer le GUI actuellement Charger
        if GUI == "CMenuGUI":
            self.set_widget(CMenuGUI(self ,self.sim_factory, self.param_factory))
        elif GUI == "CSimulationGUI":
            self.set_widget(CSimulationGUI(self ,self.sim_factory, self.param_factory))
        elif GUI == "CParameterGUI":
            self.set_widget(CParameterGUI(self ,self.sim_factory, self.param_factory))
        else:
            print("Error bad GUI parameter")
            print("GUI:",GUI)

    def set_widget(self, widget):
        # Méthode pour changer le widget afficher dans la window
        self.widget = widget
        self.setCentralWidget(self.widget)

    def exit(self):
        # Méthode pour exit
        sys.exit()


def test_SimulationGUI(window, sim_factory, param_factory):
    # Fonction Test de l'interface de Simulation

    ##### Initialisation de la simulation #####
    # Mise en place des variables
    window.param_factory.create_parameter()
    window.param_factory.ls_parameter[0].set_maxdays(2)
    window.sim_factory.create_simulation(window.param_factory.get_parameter(0))

    # Initialise l'interface de la Simulation
    window.set_widget(CSimulationGUI(window, sim_factory, param_factory))

    window.sim_factory.create_Rover(window.widget.activ_sim)


def test_ParameterGUI(window, sim_factory, param_factory):
    # Fonction Test de l'interface de Paramètrage des paramètre

    # Initialise l'interface des Paramètre
    window.set_widget(CParameterGUI(window, sim_factory, param_factory))


def test_menuGUI(window, sim_factory, param_factory):
    # Fonction Test de l'interface du Menu
    # Initialise l'interface du Menu Principale
    window.set_widget(CMenuGUI(window, sim_factory, param_factory))


def test_authentificationGUI(window, sim_factory, param_factory):
    # Fonction test de l'interface d'authentification
    pass


if __name__ == "__main__":
    HeightWindow = 700
    WidthWindow = 1200

    ##### Initialisation de la fenêtre #####
    # Initialise la routine de l'appli
    app = QApplication(sys.argv) 
    #initialise la db au démarage de l'appli
    init_db()	
    
    ########Test fenetre de login ########
    #Etape 1: Fenêtre de login 
    login = CLoginGUI()
    login.show()
    app.exec()
	#Si on rentre aucune info alors on ferme la fenêtre de connexion
    if login.user is None:
        print("Connection stopped. Application closing.")
        sys.exit()
    user = login.user  
    print(f"User login : {user.username}")
	#########################
	
	# Etape 2: lance l'appli 
    window = CMainWindow(app)

    # Setup Taille
    window.resize(WidthWindow, HeightWindow)

    ##### test button in Window ######
    #button = QPushButton("Press Me")
    #window.setCentralWidget(button)
    ##### ##### ##### ##### ##### ##### #####

    #### Initialise les factory
    sim_factory = CSimulationFactory()
    param_factory = CParameterFactory()

    #### ON link les factory à la Main Window ####
    window.set_sim_factory(sim_factory)
    window.set_param_factory(param_factory)


    #### Test Authentification GUI ####
    #test_authentificationGUI(window, sim_factory, param_factory)

    #### Test Menu GUI ####
    test_menuGUI(window, sim_factory, param_factory)

    #### Test Parameter GUI ####
    #test_ParameterGUI(window, sim_factory, param_factory)

    #### Test Simulation GUI ####
    #test_SimulationGUI(window, sim_factory, param_factory)

    ##### Code Test pour plus tard du Multithreading #####

    # Execute l'appli
    app.exec()

