#Crear un arxiu de nom user.py. En aquest arxiu s’ha de crear una class de nom user. Aquesta class ha de tindre:
# Constructor
# Atributs (mínim 6)
# Getters/Setters
# Mètode de nom salutacio on es mostren, per pantalla, totes les dades (atributs) del user.
# Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

import json

class User:
    def __init__(self, nom, age, email, usuario, password, rol):
        self.nom = nom
        self.age = age
        self.email = email
        self.usuario = usuario
        self.password = password
        self.rol = rol

    def get_nom(self):
        return self.nom

    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    def get_usuario(self):
        return self.usuario

    def get_password(self):
        return self.password

    def get_rol(self):
        return self.rol

    def set_nom(self, nom):
        self.nom = nom

    def set_age(self, age):
        self.age = age

    def set_email(self, email):
        self.email = email

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_password(self, password):
        self.password = password

    def set_rol(self, rol):
        self.rol = rol

    def saludos(self):
        print("Hola, soy", self.nom + ". Tengo", self.age, "años.")
        print("Puedes contactarme en", self.email + ". Mi usuario es", self.usuario + ".")
        print("Mi rol es", self.rol + ".")




    def to_dict(self):
        return {
            "nom": self.nom,
            "age": self.age,
            "email": self.email,
            "usuario": self.usuario,
            "password": self.password,
            "rol": self.rol
        }


myUsuario = User(nom="John Doe", age=25, email="john.doe@example.com", usuario="john_doe", password="securepass", rol="User")
myUsuario.saludos()

#formato JSON
userDiccionari = myUsuario.to_dict()
userJson = json.dumps(userDiccionari, indent=2)
print("\nObject as JSON:")
print(userJson)