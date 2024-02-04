#Crear un arxiu de nom vehicle.py. En aquest arxiu s’ha de crear una class de nom vehicle. Aquesta class ha de tindre:
# Constructor
# Atributs (mínim 6)
# Getters/Setters
# Mètode de nom parts on es mostren, per pantalla, totes les dades (atributs) del vehicle.
# Afegir el mètode to_dict(self) a les dues classes per retornar l’objecte en format json

import json

class Vehicle:
    def __init__(self, marca, modelo, anyo, color, precio, tipo):
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo
        self.color = color
        self.precio = precio
        self.tipo = tipo

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_anyo(self):
        return self.anyo

    def get_color(self):
        return self.color

    def get_precio(self):
        return self.precio

    def get_tipo(self):
        return self.tipo


    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_anyo(self, anyo):
        self.anyo = anyo

    def set_color(self, color):
        self.color = color

    def set_precio(self, precio):
        self.precio = precio

    def set_tipo(self, tipo):
        self.tipo = tipo

    def parts(self):
        print("marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("anyo: ", self.anyo)
        print("Color: ", self.color)
        print("precio: ", self.precio)
        print("Tipo: ", self.tipo)

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "anyo": self.anyo,
            "color": self.color,
            "precio": self.precio,
            "Tipo": self.tipo
        }


vehiculo = Vehicle(marca="Nissan", modelo="Kicks", anyo=2021, color="Rojo", precio=10000, tipo="hibrido")
vehiculo.parts()

vehicleDiccionari = vehiculo.to_dict()
vehicleJson = json.dumps(vehicleDiccionari, indent=2)
print("\nObject as JSON:")
print(vehicleJson)
