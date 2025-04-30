#######
# Fichier Principale
#######
import sys
import PyQt6

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QSlider, QHBoxLayout, QScrollArea


from queue import Queue 
from threading import Thread 


# Import Paramater
from src.Parameters.CParameter import CParameter
# Import Simulation
from src.Simulation.CSimulation import CSimulation
# Import GUI
from src.Menu.CMenuGUI import CMenuGUI
from src.Simulation.GUI.CSimulationGUI import CSimulationGUI



# Doit faire:
# - Mettre en place test Simulation plus poussé
# - Mettre en place la création d'une page et l'affichage des résultat dans la simulation
# - Mettre en place la séparation en thread du programme
#   2 choses:
#   --> Sépararation du process https://docs.python.org/3/library/threading.html ou https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing
#   --> Communication entre les process https://www.geeksforgeeks.org/python-communicating-between-threads-set-1/

# Rappel:
# - GUI = interface graphique
# - Controler = controler de l'interface GUI (appeler les setter)
#   --> ! Attention ! il peut y avoir plusieurs controller par classe
# - DAO = Data Access Object, transfert des données de la base de données en données utilisable en programme


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
        # On veut que la fenêtre soit montré
        self.show()

    # Setter
    def set_window_size(self, Width, Height):
        # Méthode pour set la hauteur et la largeur de la window
        self.setFixedSize(Width, Height)

    def set_widget(self, widget):
        # Méthode pour changer le widget afficher dans la window
        self.widget = widget
        self.setCentralWidget(self.widget)




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

    window.set_widget(CSimulationGUI())



    ##### Initialisation de la simulation #####
    # Mise en place des variables
    cp = CParameter()
    cp.set_maxdays(2)
    s = CSimulation(cp)
    s.factory.create_Rover()


    ##### Boucle Principales de Calcul #####
    while(s.is_end() == False):
        # On update
        s.update_hour()
        # On affiche dans le terminal
        s.afficher()
        # On redirige vers le Window text
        window.widget.add_log(s.get_rover_log())


    # Execute l'appli
    app.exec()


    ##### Code Test pour plus tard du Multithreading #####

    #





