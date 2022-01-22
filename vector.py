import math

class Vector:

    def __init__(self,x,id):
        self.id = id
        self.x = x
        self.norm = self.set_norm()
    
    def set_norm(self):
        norm = 0
        for element in self.x:
            norm = norm + pow(float(element),2)
        return math.sqrt(norm)

    def normalisation_vect(self):
        tab = []
        for element in self.x:
            element = float(element)/self.norm
            tab.append(element)
        self.set_x(tab)

    def set_x(self,tab):
        self.x  = tab

    def affiche_vect(self):
        for x in self.x:
            print(x, end=" ")
        print(self.id , self.norm)

    


