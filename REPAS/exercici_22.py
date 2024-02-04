# Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
# Un root de nom alumnos.
# Cinc childs (del root) amb nom student.
# Cada child student ha de tindre 4 subchilds:
#  name
#  surname
#  email
#  dni
# Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
# El text de cada etiqueta serà de la vostra elecció.

import xml.etree.ElementTree as ET

def crear_xml():
    estudiante = ET.Element("alumnos")

    for i in range(1, 6):
        student = ET.SubElement(estudiante, "alumno")
        student.set("id", str(i))
        name = ET.SubElement(student, "name")
        surname = ET.SubElement(student, "surname")
        email = ET.SubElement(student, "email")
        dni = ET.SubElement(student, "dni")
        name.text = f"Nombre{i}"
        surname.text = f"Apellido{i}"
        email.text = f"correo{i}@example.com"
        dni.text = f"DNI{i}"
    tree = ET.ElementTree(estudiante)
    tree.write("alumnos.xml")
    with open("alumnos.xml", "r") as file:
        print(file.read())

crear_xml()
