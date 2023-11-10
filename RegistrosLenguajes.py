import os
import csv
from csv import reader

personas = []
MenuEleccion2 = """
+------------------------------------------+
|                Buscar por                |
+------------------------------------------+
| Elige una de las siguientes opciones:    |
| [1] Nombre                               |
| [2] Apellido                             |
| [3] Edad                                 |
| [4] Lenguaje que maneja                  |
| [5] Salir                                |
+------------------------------------------+

Ingresa la opcion que deseas:
>> """

MenuEleccion1 = """
+------------------------------------------+
|                  Menu                    |
+------------------------------------------+
| Elige una de las siguientes opciones     |
| [1] Registrar                            |
| [2] Consultar                            |
| [3] Salir                                |
+------------------------------------------+

Ingresa la opcion que deseas:
>> """


def escribir(persona):
	with open("./ED/python/registros.csv", "a", newline='',
	          encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerow(persona)
	Principal()


def leer():
	global personas
	with open("./ED/python/registros.csv", "r", encoding="utf-8") as file:
		file_reader = reader(file)
		personas = [line for line in file_reader if personas != None]


def Lenguaje():
	lenguajes = []
	eleccion = input(
	 "¿Deseas ingresar un lenguaje de programacion? [Yes or Not] ").upper()
	while eleccion == "YES":
		lenguaje_ingresado = input("Escribe el lenguaje que manejas: ").capitalize()
		lenguajes.append(lenguaje_ingresado)
		eleccion = input(
		 "¿Deseas ingresar un lenguaje de programacion? [Yes or Not] ").upper()
	return lenguajes


def Registrar():
	persona = []
	print("Ingresa los siguientes datos de la persona: ")
	nombre = input("Nombre: ").title()
	apellido = input("Apellido: ").title()
	edad = int(input("Edad: "))
	lenguajes = Lenguaje()
	persona = [nombre, apellido, edad, lenguajes]
	return persona
	Principal()


def Tabla():
	bordes = f'+{"-" * 84}+'
	print(bordes)
	menu_tabla = "| NOMBRE           | APELLIDO                | EDAD     | LENGUAJES                  |"
	print(menu_tabla)
	print(bordes)


def menu_registrar():
	print("No existen personas registradas")
	agregar = input("¿Deseas agregar una persona? (Yes or Not): ").upper()
	if agregar == "YES":
		persona = Registrar()
		escribir(persona)
	elif agregar == "NOT":
		Principal()
	else:
		print("La opcion que ingresaste no es correcta, intentalo de nuevo.")
		menu_registrar()
	os.system(clear)
	Principal()


def PorNombre():
	bordes = (f'+{"-" * 84}+')
	leer()
	nombre_elegido = input(
	 "Ingresa el nombre de la persona que deseas buscar: ").title()
	if len(personas) != 0:
		Tabla()
		for persona in personas:
			if persona[0] == nombre_elegido:
				nombre, apellido, edad, lenguajes = persona
				print(
				 f'| {nombre}{" " * (16 - len(nombre))} | {apellido}{" " * (23 - len(apellido))} | {edad}{" " * (8 - len(edad))} | {lenguajes}{" " * (27 - len(lenguajes))}|'
				)
				print(bordes)
	else:
		menu_registrar()


def PorApellido():
	bordes = (f'+{"-" * 84}+')
	leer()
	apellido_elegido = input(
	 "Ingresa el apellido de la persona que deseas buscar: ").title()
	if len(personas) != 0:
		Tabla()
		for persona in personas:
			if persona[1] == apellido_elegido:
				nombre, apellido, edad, lenguajes = persona
				print(
				 f'| {nombre}{" " * (16 - len(nombre))} | {apellido}{" " * (23 - len(apellido))} | {edad}{" " * (8 - len(edad))} | {lenguajes}{" " * (27 - len(lenguajes))}|'
				)
				print(bordes)
	else:
		menu_registrar()


def PorEdad():
	bordes = (f'+{"-" * 84}+')
	leer()
	edad_elegida = input("Ingresa la edad de la persona que deseas buscar: ")
	if len(personas) != 0:
		Tabla()
		for persona in personas:
			if persona[2] == edad_elegida:
				nombre, apellido, edad, lenguajes = persona
				print(
				 f'| {nombre}{" " * (16 - len(nombre))} | {apellido}{" " * (23 - len(apellido))} | {edad}{" " * (8 - len(edad))} | {lenguajes}{" " * (27 - len(lenguajes))}|'
				)
				print(bordes)
	else:
		menu_registrar()


def PorLenguaje():
	bordes = (f'+{"-" * 84}+')
	leer()
	lenguaje_elegido = input("Ingresa el lenguaje que deseas consultar: ").title()
	if len(personas) != 0:
		Tabla()
		for persona in personas:
			if lenguaje_elegido in persona[3]:
				nombre, apellido, edad, lenguajes = persona
				program = ''
				program = [i for i in lenguajes]
				program = ''.join(program)
				program = program.replace("[", "")
				program = program.replace("]", "")
				program = program.replace("'", "")
				print(
				 f'| {nombre}{" " * (16 - len(nombre))} | {apellido}{" " * (23 - len(apellido))} | {edad}{" " * (8 - len(edad))} | {program}{" " * (27 - len(program))}|'
				)
				print(bordes)
	else:
		menu_registrar()


def Consultar():
	opcion2 = int(input(MenuEleccion2))
	if opcion2 == 1:
		PorNombre()
	elif opcion2 == 2:
		PorApellido()
	elif opcion2 == 3:
		PorEdad()
	elif opcion2 == 4:
		PorLenguaje()
	elif opcion2 == 5:
		exit()
	else:
		print("La opcion no esta dentro del menu vuelve a intentarlo.")
		os.system(clear)
		Consultar()


def Principal():
	opcion = int(input(MenuEleccion1))
	if opcion == 1:
		persona = Registrar()
		escribir(persona)
	elif opcion == 2:
		Consultar()
	elif opcion == 3:
		exit()
	else:
		print("La opcion no esta dentro del menu vuelve a intentarlo.")
		os.system(clear)
		Principal()


if __name__ == '__main__':
	if os.name == "posix":
		clear = "clear"
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		clear = "cls"
	Principal()
