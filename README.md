 # genie_logiciel
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

----------
Bibliothèque Graphique:
- Django
- PyQt


- Représentation des rovers par des icones
- Rover décomposé en plusieurs parties (roue,chassis,corps,panneau solaire, caméra, bras articulé(s))
- 2 types de Rovers:
 - Exploration
 - Collecte d'échantillon
- 2 types de Déploiement de Rovers:
  - En Constellation / dans une Zone précise avec un nombre précis
  - En Solo
- paramètre Simulation:
  - gravité
  - abrasion du sol
  - Vitesse de la Simulation
  - Rovers
     - Usure
     - Vitesse des Rovers
     - Distance de communications entre les rovers
  - Météo
     - Niveau d'alerte
     - placement des tempêtes de sables
     - radiation Solaire
     - fréquence des séisme
     - fréquence des pluies de météorites
     - Cycle Jour/Nuit
- Génération Procédurale de la Carte
  - Pouvoir Utiliser des Heightmap
  - Point d'intéret aléatoire pour les échantillons
  - Strate Rocheuse

(https://shared.cloudflare.steamstatic.com/store_item_assets/steam/apps/803050/ss_f9ef6053f923abe60d4503327800e16c597990ba.1920x1080.jpg?t=1733496904)

Bonus:
- Prise en Compte des Grottes
- Température
- Mars la bleue
- Mars la Verte
- Carte Sphère

https://www.canva.com/design/DAGgH0kv9-E/PxUw5Kih1vXR7gL8gdp84A/edit?utm_content=DAGgH0kv9-E&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
