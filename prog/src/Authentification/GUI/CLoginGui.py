########################################################################
# Fichier qui vient Contenir la Classe login GUI
# Initialiser dans User
########################################################################
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from data.db.db_utils import check_user_data, add_user
from src.Authentification.CUser import CUser

class CLoginGUI(QWidget):
	def __init__(self, parent=None):
		# Init fenetre
		super().__init__(parent)
		self.setWindowTitle("Connexion")
		self.setFixedSize(400, 250)
		
		# Ligne pour écrire son username
		self.username_label = QLabel("Nom d'utilisateur")
		self.username_input = QLineEdit()
		
		# Ligne pour écrire son mot de passe
		self.password_label = QLabel("Mot de passe")
		self.password_input = QLineEdit()
		#self.password_input.setEchoMode(QLineEdit.Password)
		
		#bouton pour se connecter
		self.login_button = QPushButton("Se connecter")
		self.login_button.clicked.connect(self.try_login)
		
		#bouton pour s'enregistrer
		self.register_button = QPushButton("S'enregistrer")
		self.register_button.clicked.connect(self.register_user)
		
		# Ajout des widgets
		layout = QVBoxLayout()
		layout.addWidget(self.username_label)
		layout.addWidget(self.username_input)
		layout.addWidget(self.password_label)
		layout.addWidget(self.password_input)
		layout.addWidget(self.login_button)
		layout.addWidget(self.register_button)
		
		self.setLayout(layout)
		self.user = None 	#CUser si la connexion réussit

	def try_login(self):
		#Tentative de login
		username = self.username_input.text()
		password = self.password_input.text()
		#Vérifie username et mdp, si true connexion et fermeture de la fenetre
		if check_user_data(username, password) == True:
			self.user = CUser(username)
			QMessageBox.information(self, "Succès", "Connexion réussie!")
			self.close()
		#Si false, message d'erreur
		else:
			QMessageBox.warning(self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect.")
    		
	def register_user(self):
		#Enregistre un user
		username = self.username_input.text()	
		password = self.password_input.text()	
		#Si l'user qui veut s'enregistrer n'existe pas alors on le crée et on ferme la fenetre
		if add_user(username, password) == True:
			QMessageBox.information(self, "Succès", "Utilisateur créé avec succès. Vous pouvez maintenant vous connecter.")
			self.accept()
		else:
			QMessageBox.warning(self, "Erreur", "Echec de l'enregistrement, le nom d'utilisateur est déjà pris.")
			
    		
    		

