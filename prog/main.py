from src.Parameters.CParameter import CParameter
from src.Simulation.CSimulation import CSimulation
cp = CParameter()
s = CSimulation(cp)
s.factory.create_Rover()

for _ in range(48):
    s.update_hour()
    s.afficher()