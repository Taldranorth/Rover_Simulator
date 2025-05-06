 # Projet simulateur de rover (Génie logiciel)
Exigence Rover:
- Doit être connecté entre eux
- Doit pouvoir gérer la perte d'un membre de manière automatique
- Doit pouvoir gérer sa trajectoire selon la topographie
- Doit pouvoir gérer le carburant/l'Usure
- Doit pouvoir gérer la positions des échantillons
- Doit pouvoir gérer un réseau de Rover

Exigence Simulation:
- Doit pouvoir sélectionner le Spawn des Rovers
- Doit pouvoir gérer la taille de la carte
- Doit pouvoir Simuler une météo basique
- Doit pouvoir gérer une carte souterraine(à définir)
- Doit pouvoir gérer la Durée de la Simulation et l'objectif
- L'utilisateur Doit pouvoir gérer des paramètres poussés de la simulation
- Doit pouvoir enregistrer un setup de pramaètres (preset)
- Doit pouvoir exporter les résultats de la simulation (fichier txt)
- Doit pouvoir sauvegarder et charger une simulation encore en cours

----------
Bibliothèque Graphique:
- PyQt6
- matplot

-psycopg2

- Rover décomposé en plusieurs parties (roue,chassis,corps,panneau solaire, caméra, bras articulé(s))
- paramètre Simulation:
  - gravité
  - Vitesse de la Simulation
  - Rovers
     - Usure
  - Météo
     - Niveau d'alerte
     - placement des tempêtes de sables
     - radiation Solaire
     - Cycle Jour/Nuit

(https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/803050/ss_f9ef6053f923abe60d4503327800e16c597990ba.1920x1080.jpg?t=1733496904)

Bonus:
- 2 types de Rovers:
	- Exploration
	- Collecte d'échantillon
- 2 types de Déploiement de Rovers:
	- En Constellation / dans une Zone précise avec un nombre précis
	- En Solo
- Vitesse des Rovers
- Distance de communications entre les rovers
- Génération Procédurale de la Carte
- Prise en Compte des Grottes
- Température
- Mars la bleue
- Mars la Verte
- Carte Sphère

Maquette :
https://www.figma.com/design/UexSkLlWyxFkILi2CTj5sc/ROVER?node-id=0-1&p=f&t=1Htd24CaO8Q0syqZ-0
https://www.canva.com/design/DAGgH0kv9-E/PxUw5Kih1vXR7gL8gdp84A/edit?utm_content=DAGgH0kv9-E&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
