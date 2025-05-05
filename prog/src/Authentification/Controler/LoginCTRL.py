########################################################################
# Fichier qui vient Contenir la Controler des Users
# Initialiser dans User
########################################################################
from src.Authentification.DAO.UserDao import check_user_data, add_user
from src.Authentification.CUser import CUser

def try_login(username, password):
	#Retourne l'attribut username de la classe Cuser si le login a réussi, None sinon
    if check_user_data(username, password) == True:
        return CUser(username)
    return None

def register_user(username, password):
	#Enregistre un nouvel user dans la database, retourne true ou false en fonciton de la réussite de la fonction
    return add_user(username, password)




