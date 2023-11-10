def obtener_prefijo(palabras):
	prefijo = ""
	for prefijos in zip(*palabras):
		if len(set(prefijos)) == 1:
			prefijo += prefijos[0]
		else:
			break
	return prefijo


def main():
	texto_entrada = input("Ingresa una cadena de palabras: ")

	texto_entrada = texto_entrada.replace("-", " ").replace(",", " ")

	palabras = texto_entrada.split()

	prefijo_comun = obtener_prefijo(palabras)

	if prefijo_comun:
		print(
		 f'El prefijo que se repite en todas la palabras es: "{prefijo_comun}".')
	else:
		print("No hay un prefijo que se repita en la lista.")


main()
