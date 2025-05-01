#######
# Fichier Principale
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

# Doit faire:
# - Mettre en place test Simulation plus poussé
# - Mettre en place la séparation en thread du programme
#   2 choses:
#   --> Sépararation du process https://docs.python.org/3/library/threading.html ou https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing
#   --> Communication entre les process https://www.geeksforgeeks.org/python-communicating-between-threads-set-1/

# Rappel:
# - GUI = interface graphique
# - Controler = controler de l'interface GUI (appeler les setter)
# - DAO = Data Access Object, transfert des données de la base de données en données utilisable en programme


# Objectif 1 mars:
# - version Basique Menu Principale
# - Mettre en place les boutons du ParameterGUI
# - linkage entre les Menu Principale,Simu et paramètre
# - Séparation en 2 threads et communication entre les threads

# Objectif 2 mars:
# - Mettre en place la sauvegarde des fichiers
#   --> Sauvegarde/Chargement des Paramètres
#   --> Sauvegarde/Chargment des Simulations
#   --> Sauvegarde des Résultats
# - Refaire Interface Simulation:
#   --> Délai lors de l'éxécutions de la boucle
#   --> Pause/Reprise de la Simulation
#   --> Menu pour accéder au différent Graphe
#   --> Refactoriser pour simplifier l'implémentation des Graphes


# Notes:
#   - Je ne suis pas sur de mon coup pour le link entre les différents GUI,
#   mais j'ai finit par mettre la main window en attribut des CTRL afin qu'il puisse y accèder est appelé les changement de
#   GUI de la main window
#       --> Par contre cela veut dire que la MainWindow garde aussi en mémoire les Singletons factory
#          --> Voir à terme par remplacer la Class CMainWindow par une Classe Applications carrément



class CMainWindow(QMainWindow):
    def __init__(self):
        # Initialiser la classe hérité
        super().__init__()
        # Initialise le titre
        self.setWindowTitle("Test Simulateur de Rover")
        # On garde une référence au widget actuellement actif
        widget = 0
        # On déplace la fenêtre en haut à gauche
        self.move(0,0)

        # On link les singletons Factory
        self.sim_factory = 0
        self.param_factory = 0
        self.user_factory = 0

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
            self.set_widget(CParameterGUI(self ,self.param_factory))
        else:
            print("Erreur Mauvais Paramètre GUI")
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

    # Initialise l'interface de la Simulation
    window.set_widget(CSimulationGUI(window, sim_factory, param_factory))



    ##### Initialisation de la simulation #####
    # Mise en place des variables
    window.widget.CTRL.create_parameter()
    window.widget.CTRL.param_factory.ls_parameter[0].set_maxdays(2)
    window.widget.CTRL.create_simulation(window.widget.CTRL.get_parameter(0))
    window.widget.CTRL.create_Rover(window.widget.activ_sim)
    s = window.widget.CTRL.get_simulation(0)

    ##### Boucle Principales de Calcul #####
    while(s.is_end() == False):
        # On update
        s.update_hour()
        # On affiche dans le terminal
        s.afficher()
        # On redirige vers le Window text
        window.widget.add_log(s.get_rover_log())



def test_ParameterGUI(window, sim_factory, param_factory):
    # Fonction Test de l'interface de Paramètrage des paramètre

    # Initialise l'interface des Paramètre
    window.set_widget(CParameterGUI(window, param_factory))




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
    window = CMainWindow()

    # Setup Taille
    window.setFixedSize(WidthWindow, HeightWindow)

    ##### test button in Window ######
    #button = QPushButton("Press Me")
    #window.setCentralWidget(button)
    ##### ##### ##### ##### ##### ##### #####

    #### Initialise les factory
    sim_factory = CSimulationFactory()
    param_factory = CParameterFactory()

    #### Test Simulation GUI ####
    #test_SimulationGUI(window, sim_factory, param_factory)

    #### Test Parameter GUI ####
    test_ParameterGUI(window, sim_factory, param_factory)

    #### Test Menu GUI ####
    #test_menuGUI(window, sim_factory, param_factory)


    #### Test Authentification GUI ####
    #test_authentificationGUI(window, sim_factory, param_factory)

    # Execute l'appli
    app.exec()


    ##### Code Test pour plus tard du Multithreading #####

    #





