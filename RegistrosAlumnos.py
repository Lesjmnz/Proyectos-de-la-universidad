lista_alumnos = []


class Alumno:

	def __init__(self, matricula, nombre, apellido_p, apellido_m, grupo,
	             promedio):
		self.matricula = matricula
		self.nombre = nombre
		self.apellido_p = apellido_p
		self.apellido_m = apellido_m
		self.grupo = grupo
		self.promedio = promedio

	def Agregar_alumno(self):
		matricula = input("Ingresa la matricula correspondiente al alumno: ")
		#SOFTWARE, AGROTECNOLOGIA
		matricula_digitos = matricula[7:13]
		assert matricula.isascii(
		), "Error: La matricula no solo puede ser de numeros o letras."
		if len(matricula) == 13:
			print("")
			if matricula[2:6] == "SOFT" or matricula[2:6] == "AGRT":
				print("")
				if matricula[:1] != "I":
					raise print("Error: La matricula debe iniciar con 'I' (Ingenieria).")
				elif matricula[1:2] != "-" or matricula[6:7] != "-":
					raise print("Error: El digito de separacion debe ser '-'.")
				elif matricula[2:6] != "SOFT":
					if matricula[2:6] != "AGRT":
						raise print(
						 "Error: El codigo de carrera de la matricula es 'AGRT' (agrotecnologia) o 'SOFT' (software)"
						)
				elif matricula_digitos.isnumeric():
					nombre = input("Ingresa el nombre: ")
					apellido_paterno = input("Ingresa el apellido paterno: ")
					apellido_materno = input("Ingresa el apellido paterno: ")
					grupo = input("Ingresa el grupo: ")
					Alumno.calificacion()

					alumno = [
					 matricula, nombre, apellido_paterno, apellido_materno, grupo, promedio
					]
					lista_alumnos.append(alumno)
					Alumno.menu_funcion()
				else:
					raise print("Error: Los ultimos digitos no son numericos.")

		#NEGOCIOS
			elif matricula[2:4] == "NA":
				matricula_digitos = matricula[5:11]
				print("")
				if matricula[:1] != "L":
					raise print("Error: La matricula debe iniciar con 'L' (Licenciatura).")
				elif matricula[1:2] != "-" or matricula[4:5] != "-":
					raise print("Error: El digito de separacion debe ser '-'.")
				elif matricula[2:4] != "NA":
					raise print(
					 "Error: El codigo de carrera de la matricula es 'AGRT' (agrotecnologia) o 'SOFT' (software)"
					)
				elif matricula_digitos.isnumeric():
					nombre = input("Ingresa el nombre: ")
					apellido_paterno = input("Ingresa el apellido paterno: ")
					apellido_materno = input("Ingresa el apellido paterno: ")
					grupo = input("Ingresa el grupo: ")
					alumno = [
					 matricula, nombre, apellido_paterno, apellido_materno, grupo, promedio
					]
					lista_alumnos.append(alumno)
					menu_funcion()
				else:
					raise print("Error: Los ultimos digitos no son numericos.")
			else:
				raise print("Error: La matricula ingresada no contiene lo necesario.")

	def Ver_tabla(self):
		bordes = ("+", ("-") * 87, "+")
		menu_tabla = "| MATRICULA           | NOMBRE(S)                | APELLIDOS                   | GRUPO            |"
		print(
		 "|                                       REGISTRO ALUMNOS                                          |"
		)
		for alumno in lista_alumnos:
			matricula, nombre, apellido_paterno, apellido_materno, grupo, promedio = alumno
			print(bordes)
			print(menu_tabla)
			print(
			 f'| {matricula}{" " * (19 - len(matricula))} | {nombre}{" " * (24 - len(nombre))} | {apellido_materno, apellido_paterno}{" " * (27 - len(apellido_paterno + apellido_materno))} | {grupo}{" " * (16 - len(grupo))} |'
			)
			print(bordes)

	def menu_funcion(self):
		menu = int(
		 input("""
  Menu de opciones:
  [1] Agregar alumno.
  [2] Mirar tabla alumnos.
  [3] salir.
  >> """))
		if menu == 1:
			Alumno.Agregar_alumno()
		elif menu == 2:
			Alumno.Ver_tabla()
		elif menu == 3:
			exit()
		else:
			print("La opcion elegida es incorrecta, vuelve a intentarlo.")
			Alumno.menu_funcion()


Alumno.menu_funcion()
