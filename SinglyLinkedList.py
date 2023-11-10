from Nodo import Node


class SLL:

    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __str__(self):
        current = self.head
        string = ""
        while current:
            if current == None:
                print(None)
            else:
                string += str(current) + " -> "
            current = current.next
        string += "None"
        return str(string)

    def __pythonlist__(self):
        if self.head is None:
            print("[]")
            return
        elementos = []
        current = self.head
        while current:
            elementos.append(str(current.data))
            current = current.next
        return print("[" + ", ".join(elementos) + "]")

    def __append__(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def __len__(self):
        return print(str(self.size))

    def __pop__(self, index=None):
        count_index = 0
        current = self.head

        if index == None:
            if current is None:
                print("No existe una lista.")

            while current:
                if current.next.next == None:
                    current.next = None
                    self.size -= 1
                    return
                current = current.next

        if index >= self.size or index < 0:
            print("El indice esta fuera de rango.")

        elif index == 0:
            current = current.next
            self.size -= 1

        elif current == None:
            print("La lista esta vacía.")

        while current:
            if count_index == index - 1:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
            count_index += 1

    def __count__(self, value):
        current = self.head
        count = 0
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return print(f'El {value} se repite {count} veces.')

    def __getnode__(self, index):
        current = self.head
        index_count = 0
        while current:
            if index_count == index:
                return print(current)
            else:
                current = current.next
                index_count += 1
        return print("None")

    def __search__(self, value):
        current = self.head
        index_count = 0

        while current:
            if current.data == value:
                print(
                    f'El valor {value} se encuentra en el indice {index_count}.'
                )
                return
            current = current.next
            index_count += 1
        return print(f'El valor {value} no se encontro en la lista.')

    def __sort__(self):
        elements = []
        current = self.head

        if current == None:
            print("La lista está vacía. No hay elementos para ordenar.")
            return

        while current:
            elements.append(current.data)
            current = current.next
        elements.sort()

        current = self.head
        for value in elements:
            current.data = value
            current = current.next


#TERMINARLOS

    def __insert__(self, index, new_value):

        if index < 0 or index > self.size:
            print("El indice esta fuera del rango.")
            return

        new_node = Node(new_value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            #while current.next != None or index < self.size:
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def __remove__(self, value):
        current = self.head

        if current is None:
            print("La lista esta vacia.")
            return

        if current.data == value:
            self.head = current.next
            self.size -= 1
            return

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

        print(f'No existe {value} en la lista.')

    def __iter__(self):
        current = self.head
        while current is not None:
            data = current.data
            current = current.next
            yield data  #yield es como un contenedor pero no guarda todo, genera unas pausas hasta que lo vuelvas a llamar, su valor cambia conforme lo llames
            #es decir si tu tienes 3 yield y en cada uno un numero (1, 2, 3), cuando llamas a yield en pausas eset llama uno por uno el numero
            #no funciona como la variable, guarda los valores pero despues como que los olvida y solo los puedes usar cuando los llamas aunque hace una tipo pausa
            #no como en el return que si lo usas te hace un stop pero en el yield es mas como una pausa

lista = SLL()
lista.__append__(1)
lista.__append__(2)
lista.__append__(3)
lista.__append__(4)
lista.__append__(1)
lista.__append__(2)
lista.__append__(3)
lista.__append__(4)
print(lista)
lista.__len__()
lista.__pythonlist__()
lista.__pop__()
print(lista)
lista.__pop__(2)
print(lista)
lista.__getnode__(0)
lista.__count__(2)
lista.__insert__(0, 5)
print(lista)
lista.__len__()
lista.__insert__(2, 8)
print(lista)
lista.__search__(2)
lista.__sort__()
print(lista)
lista.__len__()
lista.__remove__(1)
print(lista)
lista.__remove__(5)
print(lista)
lista.__remove__(0)
print(lista)
