########################################################################
# Fichier qui vient Contenir la Classe login GUI
# Initialiser dans User
########################################################################
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from src.Authentification.Controler.LoginCTRL import try_login, register_user

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
		self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
		
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
		user = try_login(username, password)
		if user:
			self.user = user
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
		if register_user(username, password):
			QMessageBox.information(self, "Succès", "Utilisateur créé avec succès. Vous pouvez maintenant vous connecter.")
		else:
			QMessageBox.warning(self, "Erreur", "Echec de l'enregistrement, le nom d'utilisateur est déjà pris.")
			
    		
    		

