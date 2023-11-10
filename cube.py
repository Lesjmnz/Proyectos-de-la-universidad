from Arreglo import Arreglo
from Grid import Grid
import random


class Cube():

    def __init__(self, rows, col, depth):
        self.data = Grid(rows, col)
        for row in range(self.__height__()):
            for col in range(self.__wide__()):
                self.data[row][col] = Arreglo(depth)

    def __str__(self):
        tensor = ""

        for depth in range(self.__depth__()):
            tensor += f'profundidad {depth} \n'
            for row in range(self.__height__()):
                for col in range(self.__wide__()):
                    tensor += str(self.data[row][col][depth]) + " "
                tensor += "\n"
            tensor += "\n"
        return str(tensor)

    def __height__(self):
        return self.data.__height__()

    def __wide__(self):
        return self.data.__wide__()

    def __depth__(self):
        return len(self.data[0][0])

    def __setitem__(self, row, col, dep, new_item):
        self.data[row][col][dep] = new_item

    def __getitem__(self, row, col, dep):
        return self.data[row][col][dep]

    def __delete__(self, row, col, dep):
        self.data[row][col][dep] = None

    def __random_fill__(self, num_min, num_max):
        for depth in range(self.__depth__()):
            for col in range(self.__wide__()):
                for row in range(self.__height__()):
                    self.data[row][col][depth] = random.randint(
                        num_min, num_max)

    def __index__(self, item):
        for depth in range(self.__depth__()):
            for row in range(self.__height__()):
                for col in range(self.__wide__()):
                    if self.data[row][col][depth] == item:
                        return print(
                            f'Fila: {row}, columna: {col}, profundidad: {depth}'
                        )

    def __count__(self, item):
        count = 0
        for depth in range(self.__depth__()):
            for row in range(self.__height__()):
                for col in range(self.__wide__()):
                    if self.data[row][col][depth] == item:
                        count += 1
        return print(f'El {item} se repite {str(count)}')

    def __fill__(self):
        count = 1
        for deep in range(self.__depth__()):
            for row in range(self.__height__()):
                for col in range(self.__wide__()):
                    self.data[row][col][deep] = count
                    count += 1

    def __clr__(self):
        for deep in range(self.__depth__()):
            for row in range(self.__height__()):
                for col in range(self.__wide__()):
                    self.data[row][col][deep] = None

    def __getrow__(self, row, depth):
        string = ""
        for col in range(self.__wide__()):
            string += str(self.data[row][col][depth]) + " "
        return string

    def __getcol__(self, col, depth):
        string = ""
        for row in range(self.__height__()):
            string += str(self.data[row][col][depth]) + "\n"
        return string

    def __get_col_row_from_depth__(self, depth):
        string = ""
        for row in range(self.__height__()):
            for col in range(self.__wide__()):
                string += str(self.data[row][col][depth]) + " "
            string += "\n"
        return string

    def __sort__(self):
        self.datos = []
        count_1 = 0
        for col in range(self.__wide__()):
            for row in range(self.__height__()):
                for depth in range(self.__depth__()):
                    if self.data[row][col][depth] is not None:
                        self.datos.append(self.data[row][col][depth])
                    else:
                        count_1 += 1
        self.datos.sort()
        count = 0
        for row in range(self.__height__()):
            for col in range(self.__wide__()):
                for depth in range(self.__depth__()):
                    if count_1 != 0:
                        self.data[row][col][depth] = None
                        count_1 -= 1
                    else:
                        self.data[row][col][depth] = self.datos[count]
                        count += 1


if __name__ == __name__:
  pass
