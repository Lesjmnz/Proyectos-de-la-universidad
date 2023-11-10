def decorator(func):

	def nested(numero):
		resultado = func(numero)
		return resultado

	return nested


@decorator
def numero_romanos(numero):
	numero_romanos = {
	 'I': 1,
	 'V': 5,
	 'X': 10,
	 'L': 50,
	 'C': 100,
	 'D': 500,
	 'M': 1000
	}
	resultado = 0

	for i in range(len(numero)):
		if i > 0 and numero_romanos[numero[i]] > numero_romanos[numero[i - 1]]:
			resultado += numero_romanos[numero[i]] - 2 * numero_romanos[numero[i - 1]]
		else:
			resultado += numero_romanos[numero[i]]

	return resultado


numero = input(
 "Ingresa el numero que deseas pasar a entero usando [I, V, X, L, C, D, M]: "
).upper()

print(numero_romanos(numero))
