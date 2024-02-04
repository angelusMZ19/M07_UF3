# Crear una funció que llegeixi el JSON de l’exercici anterior  i surti el resultat (en format json) per consola.

import json

def leeJson():
    with open("books.json", "r") as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=2))
leeJson()
