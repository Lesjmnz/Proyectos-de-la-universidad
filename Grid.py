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
            for column in range(len(self.items[row])):
                string += str(self.items[row][column]) + " "
            string += "\n"
        return str(string)

    def __height__(self):
        return self.items.__len__()

    def __wide__(self):
        return self.items[0].__len__()

    def __setitem__(self, row, column, value):
        self.items[row][column] = value

    def __getitem__(self, row):
        return self.items[row]

    def __deleteitem__(self, row, column):
        self.items[row][column] = None

    def __cls__(self):
        for row in range(self.__height__()):
            for column in range(self.__wide__()):
                self.items[row][column] = None

    def __fill__(self):
        c = 1
        for row in range(self.__height__()):
            for column in range(self.__wide__()):
                self.items[row][column] = c
                c += 1

    def __fillrandom__(self, numero_minimo, numero_maximo):
        for column in range(self.__wide__()):
            for row in range(self.__height__()):
                self.items[row][column] = random.randint(
                    numero_minimo, numero_maximo)

    def __getrow__(self, row):
        self.row = ""
        for i in self.items[row]:
            self.row += str(i) + " "
        return self.row

    def __getcolumn__(self, col):  #obtiene la columna que el usuario solicite
        self.col = ""  #aqui se guardaran los datos de la columna solicitada como una string
        for item in range(
                len(self.items
                    )):  #por cada elemento para el rango de la longitud de
            self.col += str(self.items[item][col]) + "\n"
        return self.col

    def __sort__(self):
        self.data = []  #aqui se guardaran los valores como si fuera una lista
        count_1 = 0
        for col in range(self.__wide__()):
            for row in range(self.__height__()):
                if self.items[row][col] is not None:
                    self.data.append(self.items[row][col])
                else:
                    count_1 += 1
        self.data.sort()
        count = 0
        for row in range(self.__height__()):
            for col in range(self.__wide__()):
                if count_1 != 0:
                    self.items[row][col] = None
                    count_1 -= 1
                else:
                    self.items[row][col] = self.data[count]
                    count += 1

    def __index__(self, item):
        for row in range(self.__height__()):
            for col in range(self.__wide__()):
                if self.items[row][col] == item:
                    return print(f'Fila: {row}, columna: {col}')

    def __count__(self, item):
        count = 0
        for row in range(self.__height__()):
            for col in range(self.__wide__()):
                if self.items[row][col] == item:
                    count += 1
        return f'El {item} aparece {count} veces'


if __name__ == __name__:
    pass
