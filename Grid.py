#altura, anchura, guardar valor, ver valor, borrar valor, borrar todo, rellenar secuencialmente, rellenar aleatoriamente, obtener valores de fila y columna, 

from Arreglo import Arreglo

import random
class Grid():
    
    def __init__(self, rows, columns):
        self.items = Arreglo(rows)
        for row in range(rows):
            self.items[row] = Arreglo(columns)
            
    def __str__(self):
        string = ""
        for row in range(self.items.__len__()):
            for col in range(len(self.items[row])):
                string += str(self.items[row][col]) + " "
            string += "\n"
        return str(string)
    
if __name__ == __name__:
    matriz = Grid(4,5)
    print(matriz)