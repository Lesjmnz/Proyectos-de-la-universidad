class calculadora:

	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.resultado = 0

	def __str__(self):
		return f'Los numeros calculados son {self.a} y {self.b}'

	def suma(self):
		self.resultado = self.a + self.b
		self.operacion = 'Suma'
		operacion.dar_resultado()

	def resta(self):
		self.resultado = self.a - self.b
		self.operacion = 'Resta'
		operacion.dar_resultado()

	def multiplicacion(self):
		self.resultado = self.a * self.b
		self.operacion = 'Multiplicacion'
		operacion.dar_resultado()

	def division(self):
		self.resultado = self.a / self.b
		self.operacion = 'Division'
		operacion.dar_resultado()

	def dar_resultado(self):
		print(f'La {self.operacion} es {self.resultado}')


a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))

operacion = calculadora(a, b)

menu = int(
 input("""Ingresa la opcion correspodiente a lo que buscas
[1] Suma
[2] Resta
[3] Multiplicacion
[4] Division
>> """))

if menu == 1:
	operacion.suma()
elif menu == 2:
	operacion.resta()
elif menu == 3:
	operacion.multiplicacion()
elif menu == 4:
	operacion.division()
else:
	print("Ninguna de las opciones esta en el menu")
