import time


class Usuario:

	def __init__(self, nombre, apellido, direccion, telefono, metodo_pago,
	             ubicacion):
		self.nombre = nombre
		self.apellido = apellido
		self.direccion = direccion
		self.telefono = telefono
		self.metodo_pago = metodo_pago
		self.puntuacion = 0
		self.viajes = []
		self.ubicacion = ubicacion

	def __str__(self):
		return f'{self.nombre} {self.apellido}'

	def solicitar(self, origen, destino, tipo_servicio):
		solicitud = SolicitarViaje(self, origen, destino, tipo_servicio)
		self.solicitud = solicitud
		print(
		 f'Solicitando viaje de {self.__str__()} de {solicitud.origen} a {solicitud.destino}'
		)
		conductor = solicitud.asignar_conductor()
		if conductor:
			print(f'{conductor} esta en camino a su ubicacion')
		else:
			print("No hay conductores disponibles por el momento, intentelo mas tarde")

	def calificar(self, conductor, solicitud):
		print("Calificando")
		self.comentar(conductor, solicitud)

	def comentar(self, conductor, solicitud):
		conductor.comentarios.append('Buen servicio')


class Conductor:

	def __init__(self, nombre, apellido, telefono, auto):
		self.nombre = nombre
		self.apellido = apellido
		self.telefono = telefono
		self.auto = auto
		self.puntuacion = 0
		self.viajes = []
		self.comentarios = []
		self.disponible = True

	def __str__(self):
		return f'{self.nombre} {self.apellido}'

	def aceptar_viaje(self, solicitud):
		print(f'{self.__str__()} ha aceptado el servicio')
		self.disponible = False
		solicitud.conductor = self

	def finalizar_viaje(self, usuario, solicitud):
		print("Viaje completado")
		self.viajes.append(solicitud)
		self.disponible = True
		usuario.calificar(self, solicitud)

	def cancelar_viaje(self, solicitud):
		print("Viaje cancelado")
		self.disponible = True


class SolicitarViaje:

	def __init__(self, usuario, origen, destino, tipo_servicio):
		self.usuario = usuario
		self.origen = origen
		self.destino = destino
		self.tipo_servicio = tipo_servicio
		self.tarifa = 0
		self.conductor = None
		self.finalizado = False

	def asignar_conductor(self):
		for conductor in conductores:
			if conductor.auto.tipo_servicio == self.tipo_servicio and conductor.disponible:
				conductor.aceptar_viaje(self)
				return conductor
			return None

	def en_curso(self):
		pass


class Carro:

	def __init__(self, marca, modelo, placa, color, año, tipo_servicio):
		self.marca = marca
		self.modelo = modelo
		self.placa = placa
		self.color = color
		self.año = año
		self.tipo_servicio = tipo_servicio


class Servicio:

	def __init__(self, nombre, tarifa_base):
		self.nombre = nombre
		self.tarifa_base = tarifa_base


usuario_1 = Usuario('Lesly',
                    'Jimenez',
                    'Insurgentes',
                    '3113737045',
                    'Efectivo',
                    ubicacion=True)

usuario_2 = Usuario('Adiel',
                    'Delgado',
                    'Calle Israel',
                    '3115485256',
                    'Tarjeta',
                    ubicacion=True)

UberPoo1 = Servicio('UberPool', 65)
UberX = Servicio('UberX', 40)
carro_1 = Carro('Nissan', 'Versa', 'FXN-23-24', 'Rojo', 2019, UberX)
conductor_1 = Conductor('Luis', 'Jimenez', '3111455241', carro_1)
conductores = [conductor_1]
if usuario_1.ubicacion:
	usuario_1.solicitar('El ahuacate', 'San Blas', UberX)
	conductor_1.finalizar_viaje(usuario_1, usuario_1.solicitud)
	print(conductor_1.viajes)
else:
	print("Debes tener la ubicacion encendida")
