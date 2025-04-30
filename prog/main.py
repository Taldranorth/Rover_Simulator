#######
# Fichier Principale
#######
import sys
import PyQt6

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

# Import Paramater
from src.Parameters.CParameter import CParameter
# Import Simulation
from src.Simulation.CSimulation import CSimulation
# Import Menu
from src.Menu.CMenuGUI import CMenuGUI

# Doit faire:
# - Mettre en place test Simulation plus poussé
# - Mettre en place la création d'une page et l'affichage des résultat dans la simulation

# Rappel:
# - GUI = interface graphique
# - Controler = controler de l'interface GUI (appeler les setter)
# - DAO = Data Access Object, transfert des données de la base de données en données utilisable en programme

if __name__ == "__main__":

    HeightWindow = 700
    WidthWindow = 1200


    ##### Initialisation de la fenêtre #####
    # Initialise la routine de l'appli
    app = QApplication(sys.argv) 
    # Initialise la window
    window = QMainWindow()
    # Indique que l'on veut montrer la window
    window.show()

    # Setup Nom
    window.setWindowTitle("Test Simulateur de Rover")

    # Setup Taille
    window.setFixedSize(WidthWindow, HeightWindow)

    ##### test button in Window ######
    #button = QPushButton("Press Me")
    #window.setCentralWidget(button)
    ##### ##### ##### ##### ##### ##### #####

    #### Setup Window Text ####



    #### Setup Scrollbar ####



    ######


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



    # Execute l'appli
    app.exec()