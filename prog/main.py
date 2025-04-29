#######
# Fichier Principale
#######
from src.Parameters.CParameter import CParameter
from src.Simulation.CSimulation import CSimulation

# Doit faire:
# - Mettre en place test Simulation plus poussé
# - Mettre en place la création d'une page et l'affichage des résultat dans la simulation



if __name__ == "__main__":

    # Mise en place des variables
    cp = CParameter()
    cp.set_maxdays(2)
    s = CSimulation(cp)
    s.factory.create_Rover()



    while(s.is_end() == False):
        s.update_hour()
        s.afficher()