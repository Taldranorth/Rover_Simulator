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
		self.setWindowTitle("Connection")
		self.setFixedSize(400, 250)
		
		# Ligne pour écrire son username
		self.username_label = QLabel("Username")
		self.username_input = QLineEdit()
		
		# Ligne pour écrire son mot de passe
		self.password_label = QLabel("Password")
		self.password_input = QLineEdit()
		self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
		
		#bouton pour se connecter
		self.login_button = QPushButton("Login")
		self.login_button.clicked.connect(self.try_login)
		
		#bouton pour s'enregistrer
		self.register_button = QPushButton("Register")
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
			QMessageBox.information(self, "Success", "Connection done!")
			self.close()
		#Si false, message d'erreur
		else:
			QMessageBox.warning(self, "Error", "Incorrect password or username.")
    		
	def register_user(self):
		#Enregistre un user
		username = self.username_input.text()	
		password = self.password_input.text()	
		#Si l'user qui veut s'enregistrer n'existe pas alors on le crée et on ferme la fenetre
		if register_user(username, password):
			QMessageBox.information(self, "Success", "User register with success. Now you can login.")
		else:
			QMessageBox.warning(self, "Error", "Register failure, username already taken.")
			
    		
    		

