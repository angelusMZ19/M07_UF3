#Crear una funció que mostri, per consola, i guardi en un arxiu extern, un JSON amb una key de nom book que contindrà titel, cover, year i pages. Dintre del JSON hi hauran 4 de cada book (s’ha d’omplir amb values). 


import json
def creajson():
    books = [
        {"title": "Metamorfosis", "cover": "Portada.jpg", "year": 1915, "pages": 256},
        {"title": "Crimen y Castigo", "cover": "Portadita.jpg", "year": 1866, "pages": 532}]
    
    data = {"book": books}
    json_string = json.dumps(data, indent=2)
    print(json_string)
    with open("books.json", "w") as json_file:
        json.dump(data, json_file, indent=2)

creajson()
