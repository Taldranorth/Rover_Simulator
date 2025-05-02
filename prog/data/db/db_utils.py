#Fichier qui gère la base de données 

import psycopg2
from psycopg2 import sql, errors
from dotenv import load_dotenv
import os
import hashlib

#Charge les variable de connection depuis le fichier .env pour éviter fuite des data de connection
load_dotenv()
print("Host:", os.getenv("DB_HOST"))  # vérifie que c'est bien db.yonrlezqjzcxnvscpgow.supabase.co
print("DB Name:", os.getenv("DB_NAME"))
print("DB User:", os.getenv("DB_USER"))
print("DB SSL:", os.getenv("DB_SSL"))


#Initialisation des data pour se connecter à la base
CONFIG = {
	"host": os.getenv("DB_HOST"),
	"database": os.getenv("DB_NAME"),
	"user": os.getenv("DB_USER"),
	"password": os.getenv("DB_PASS"),
	"port": 5432,
	"sslmode": "require" if os.getenv("DB_SSL")=="true" else "disable"
}


def hash_password(password):
    #Retourne un hash SHA256 du mot de passe
    return hashlib.sha256(password.encode()).hexdigest()


def get_connection():
	#Connection a la base de données
	return psycopg2.connect(**CONFIG)


def init_db():
	#Crée la table si elle n'existe pas avec les données id, username et mot de passe
	print("Tentative de connexion à la base")
	with get_connection() as conn:
		with conn.cursor() as cur:
			cur.execute("""	
				CREATE TABLE IF NOT EXISTS users(
					id SERIAL PRIMARY KEY,
					username VARCHAR(20) UNIQUE NOT NULL,
					password VARCHAR(250) NOT NULL)
			""")
			conn.commit()
	print("Connexion à la Base réussie")
			

def add_user(username, password):
	#Ajoute un utilisateur qui a choisi son nom et son mot de passe dans la base et retourne un booléen pour vérifier la création
	try:
		with get_connection() as conn:
			with conn.cursor() as cur:
				hashed_pwd = hash_password(password)
				cur.execute("""
					INSERT INTO users(username, password) 
					VALUES (%s, %s)""", (username, hashed_pwd))
				conn.commit()
				return True
	#Si le username rentré existe déjà
	except errors.UniqueViolation:
		return False
	#Autre erreur d'ajout
	except Exception as err:
		print("Erreur lors de l'ajout de l'utilisateur :", err)
		return False 	
		

def check_user_data(username, password):
	#Renvoie True si le username et le mdp correspond à une entrée dans la base, False sinon
	with get_connection() as conn:
		with conn.cursor() as cur:
			hashed_pwd = hash_password(password)
			cur.execute("""
				SELECT * 
				FROM users 
				WHERE username = %s 
				AND password = %s""", (username, hashed_pwd))
			result = cur.fetchone()
			if result is not None:
				return True
			else:
				return False
	
					
					
					
					
					
					
					
					
	
