import random

class Arreglo:
    
    def __init__(self, capacidad, fill_value=None):
        self.items = list()
        for i in range(capacidad):
            self.items.append(fill_value)
            
    def __str__(self):
        string = ""
        for i in self.items.__iter__():
            string += str(i) + " "
        return str(string)
    
    def __fill__(self):
        for i in range(len(self.items)):
            self.items[i] = i + 1
            
    def __setitem__(self, index, new_item):
        self.items[index] = new_item
        
    def __getitem__(self, index):
        return self.items[index]
    
    def __delete__(self,index):
        self.items[index] = None
        
    def __len__(self):
        return len(self.items)
    
    def __clr__(self):
        for i in range(len(self.items)):
            self.items[i] = None
            
    def __iter__(self):
        return iter(self.items)
    
    def __count__(self, item):
        return self.items.count(item)
    
    def __index__(self, item):
        return self.items.index(item)
    
    def __sort__(self):
        self.items.sort()
        return str(self.items)
    
    def random_fill(self):
        for i in range(len(self.items)):
            self.items[i] = random.randint(1, 9)
        
if __name__ == __name__:
    pass