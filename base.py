from vector import Vector

class Base:
    def __init__(self,fichier):
        self.fichier=fichier
        self.row = 0
        self.col = 0
        self.vect = []
       
    def remplire_vect(self):
        f = open(self.fichier,"r")
        tab = []
        for line in f:
            self.col = len(line.split(","))-1
            self.row = self.row+1
            for element in line.split(","):
                tab.append(element.replace('\n',''))
            self.vect.append( Vector([tab[0],tab[1],tab[2],tab[3]],tab[4]) )  
            tab = []    
        f.close()

    def affichage_base(self):
        print("row =",self.row)
        print("col = ",self.col)
        for vect in self.vect:
            vect.affiche_vect()

    def normalisation_base(self):
        for vect in self.vect:
            vect.normalisation_vect()

    def moyenne(self):
        tab = []
        i=0
        for i in range(int(self.col)):
            tab.append(0)
        for vect in self.vect:
            for i in range(self.col):
                tab[i] = tab[i] + float(vect.x[i])
        for i in range(int(self.col)):
            tab[i] = tab[i]/float(self.row)
        return tab

