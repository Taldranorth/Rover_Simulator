# Rapport de Projet Rover  
*by Dixon Joshua / Chaudet Fearghal / Bourdon Kilian*  

## Table des matières  
- [Introduction](#introduction)  
- [1. Axe Fonctionnel](#1-axe-fonctionnel)  
  - [a. Exigences](#a-exigences)  
  - [b. Acteurs](#b-acteurs)  
  - [c. Diagramme UML](#c-diagramme-uml)  
  - [d. Scénario Nominal](#d-scénario-nominal)  
  - [e. Diagramme de Séquence](#e-diagramme-de-séquence)  
- [2. Axe Statique](#2-axe-statique)  
- [3. Projets](#3-projets)
  - [a. Dépendances et Technologies](#a-dépendances-et-technologies)
  - [b. Utiliser l'application ](#b-utiliser-lapplication )
  - [c. Répartition des tâches](#c-répartition-des-tâches)
  - [d. Améliorations Possibles](#d-améliorations-possibles)
  - [e. Problèmes rencontrés](#e-problèmes-rencontrés)
- [Conclusion](#conclusion)   

---

## Introduction  
Ce rapport présente notre projet de simulation de rovers. Nous détaillons la conception et le développement en trois axes principaux : **statique**, **fonctionnel**, et **dynamique**.  

L'objectif du projet est de simuler l'exploration autonome de rovers sur un terrain extraterrestre. Les rovers doivent être capables de collaborer, de s’adapter aux contraintes du terrain et de gérer diverses ressources.  

---

## 1. Axe Fonctionnel  

### a. Exigences  
Afin de définir le cadre du projet, nous avons établis une liste des exigences essentielles.  

#### **Exigences des Rovers**  
- Doivent être connecté entre eux​
- Doit pouvoir gérer la perte d'un membre de manière automatique​
- Doit pouvoir gérer sa trajectoire selon la topographie​
- Doit pouvoir gérer l'usure​
- Doit pouvoir gérer la position des échantillons​
- Doit pouvoir gérer un réseau de Rover

#### **Exigences de la Simulation**  
- L'utilisateur doit pouvoir sélectionner le spawn des Rovers ​
- L'utilisateur doit pouvoir gérer la taille de la carte ​
- L'utilisateur doit pouvoir simuler une météo basique ​
- L'utilisateur doit pouvoir gérer la durée de la simulation ​
- L'utilisateur doit pouvoir gérer des paramètres poussés de la simulation ​
- L'utilisateur doit pouvoir enregistrer un setup de paramètres (preset) ​
- L'utilisateur doit pouvoir exporter les résultats de la simulation (fichier .txt) ​
- L'utilisateur doit pouvoir sauvegarder et charger une simulation 

---

### c. Maquettage
Nous avons procédé a un maquettage:
Pour ce faire nous nous sommes inspiré de *Per Aspera* un jeu Tlön Industries, pour en savoir plus [ici](https://store.steampowered.com/app/803050/Per_Aspera/). 

Le jeu ressemble a ceci:

<img src="./doc/imageMaquettage/Maquettage.jpg" alt="Mar" width="600px" height="350px">

Grâce a ceci nous avons réalisé la première version qui est notre vision complète mais peu realiste :

<img src="./doc/imageMaquettage/maquette1.png" alt="Mar" width="600px" height="350px">

Deuxième version plus réaliste :

<img src="./doc/imageMaquettage/maquettage_login.png" alt="Mar" width="500px" height="350px">
<img src="./doc/imageMaquettage/maquettage_mainmenu.png" alt="Mar" width="500px" height="350px">
<img src="./doc/imageMaquettage/maquettage_parameter.png" alt="Mar" width="500px" height="350px">
---

### b. Acteurs  
Nous avons identifié les principaux acteurs intervenant dans la simulation :  
![Acteurs](./doc/imageRendu/Acteur.png)  

---

### c. Diagramme UML  
Nous avons réalisé un premier diagramme UML (L1) pour représenter l’utilisateur principal du système :  
![Diagramme UML LL1](./doc/imageRendu/DiagUC_v1.png)  

Ce premier diagramme nous a permis d'affiner notre modèle et de proposer une version améliorée (L2) :  
![Diagramme UML LL2](./doc/imageRendu/DiagUC_v2.png) 

---

### d. Scénario Nominal  
Nous avons défini un **scénario nominal** pour illustrer le processus standard d'utilisation du système.  
#### **Scénario nominal : Lancer une simulation**  
1. Le client accède au serveur
2. Le client s'authentifie sur le serveur
3. Le serveur autorise l'authentification
4. Le client configure sa simulation (choisit le temps, la météo, etc)
5. Le serveur sauvegarde les paramètres
6. Le client augmente la durabilité des roues
7. Le serveur sauvegarde le paramètre
8. Le client veut sauvegarde ses paramètre définis pour plus tard localement
9. Le serveur renvoie un fichier data au client
10. Le client lance la simulation
11. Le client modifie la résistance d'un rover
12. Le serveur sauvegarde la modification
14. Le client sauvegarde la simulation
15. Le serveur crée un nouvel emplacement pour stocker la sauvegarde
16. Après validation de la sauvegarde par le serveur le client peut exporter les résultats de la simulation 

#### **Exceptions**  
- **E1 : Serveur indisponible ou inexistant**  
  - Le client ne peut pas accéder au serveur.  
  - Un message d’erreur est affiché expliquant la raison.  

- **E2 : Échec d’authentification**  
  - Le serveur renvoie un message d’échec.
  - Le serveur autorise un nouvel essai de connexion
  - Le client doit resaisir ses identifiants tant qu'ils sont éronnés

#### **Alternatives**
- **Alt1 : Modification de la résistance sur plusieurs rovers**
  - Le client modifie la résistance de plusieurs rovers
---

### e. Diagramme de Séquence  
Le scénario nominal nous a permis de concevoir un **diagramme de séquence** décrivant les interactions entre les différentes entités :  

![Diagramme de Séquence](./doc/imageRendu/DiagSeq_EN.png)  

---

## 2. Axe Statique
L'axe fonctionnel nous a permis de mettre en place les différentes faces du projet qui nous a menés à créer ce **diagramme de classe**:

![Diagramme de Classe](./doc/imageRendu/DiagClass.png)  
---



## 3. Projets

### a. Dépendances et Technologies

Technologie Utilisé : *python3*, *Markdown*

Dépendances nécessaires: *PyQT6*, *Psycopg2*

Pour les installer:

#### - **PyQt6**

**Via terminal** (pip) :
```bash
pip install PyQt6
```

*GitHub* (documentation officielle) :  
https://github.com/PyQt/PyQt6

**Documentation détaillée** :  
https://www.riverbankcomputing.com/static/Docs/PyQt6/

---

#### - **psycopg2**

**Via terminal** (pip) :
```bash
pip install psycopg2-binary
```
(La version `psycopg2-binary` est souvent recommandée pour éviter d’avoir à compiler)

**GitHub** :  
https://github.com/psycopg/psycopg2

**Documentation officielle** :  
https://www.psycopg.org/docs/

### b. Utiliser l'application

Pour lancer le projet à partir de la source, faire :

```bash 
python3 prog/main.py 
```

Une fois dans l'app il vous suffit de créer un compte grâce a cette page: 

![Connexion](./doc/imageAppli/Page_connexion.png)

Vous pouvez creer votre première Simulation !

<img src="./doc/imageAppli/Menu.png" alt="Mar" width="600px" height="350px">

Ici vous modifier vos paramètres, *Attention* il faut bien appuyer sur **entrer** quand vous validez vos changements :

<img src="./doc/imageAppli/Parametres.png" alt="Mar" width="600px" height="350px">

Après avoir cliqué sur start il vous suffit d'ajouter des Rovers et launch la simulation.

<img src="./doc/imageAppli/launch.png" alt="Mar" width="600px" height="350px">

Après avoir attendu 30s (ou plus en fonction du nombres de jour de la sim), vous pouvez retrouvez les graphes globaux ou spécifiques aux rovers en alternant entre les tabs. Il est alors possible de sauvegarder votre simulation, de quitter l'application et même de retourner au menu principal pour créer une nouvelle simulation avec des paramètres différents !

---
### c. Répartition des tâches

|   | Kilian  | Fearghal | Joshua |
| :--------------- |:---------------:| :-----:| :-----:|
| Conception | X | X | X |
| Maquettage | | X | X |
| Implémentation | - | - | - |
| Simulation |  | X | X |
| GUI |  | X | |
| Authentification | X |  |  |

---
## d. Améliorations Possibles

- Séparation des processus en Serveur/Client avec autant de client qui peuvent se connecter au Serveur

- Compléter Manage Result en permettant d'Exporter les résultats des simulations dans un fichier .pdf Latex

- Ajout d'un Paramètre Délai et séparer le thread de Calcul de la boucle de Simulation, afin de pouvoir mettre en pause la Simulation une fois lancé

- Améliorer les paramètres de la Simulation

- Gérer la Position des Rovers sur une Carte créée aléatoirement

---

### e. Problèmes rencontrés

- Séparation multi-thread 
  
- Difficulté lors de la création du diagramme de classe: première rencontre avec les termes Factory, DAO, CTRL, ...
  
- Retranscription du diagramme de Classe

---

## Conclusion  
Ce projet de simulation de rover nous a permis de mettre en pratique un ensemble varié de compétences, que ce soit sur le plan technique ou méthodologique. En partant d’un projet clair : simuler l’exploration autonome de rovers. Nous avons donc conçu une architecture logicielle cohérente, construit une interface utilisateur fonctionnelle et mis en œuvre une logique de simulation.

Nous avons rencontrés plusieurs défis, notamment la gestion du multithreading, la conception d’un diagramme de classes structuré, et l’intégration des différentes composantes du système.

Il y a toujours des perspectives d’améliorations , que ce soit en termes de performance, de modularité (client-serveur), ou une visualisation 2D de la simulation. Cepandant les fonds pour continuer l'implémentation n'était pas suffisants, les développeurs ont donc du quitter le projet.

Enfin, cette expérience a renforcé notre compréhension du travail en équipe (notamment sur comment utiliser la méthode agile à notre avantage) dans un contexte de développement logiciel.
