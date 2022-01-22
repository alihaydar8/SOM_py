import random
import math

class Node:
    def __init__(self,w):
        self.etiquet = "*"
        # self.activ = 0
        self.w = w

class Bmu:
    def __init__(self,i,j):
        self.ligne = i
        self.colonne = j

class Network:
    def __init__(self,map_row,map_col,donne_size,moyenne,delai):
        self.col = map_col
        self.row = map_row
        self.size = donne_size
        self.maps = self.set_maps(moyenne,delai)
        self.bmu = []

    def set_maps(self,moyenne,delai):
        tab = []
        maps = []
        for i in range(self.row):
            for j in range(self.col):  
                for k in range(self.size):
                    tab.append(random.uniform(float(moyenne[k])-delai, float(moyenne[k]+delai)))   
                maps.append(Node(tab))
                tab = []
        return maps

    def get_index(self,index):
        i = int(index/self.col)
        j = index - i*self.col
        return Bmu(i,j)

    def get_maps(self,i,j):
        return self.maps[i*self.col +j]

    def affiche_network(self):
        s = 0
        g = 0
        o = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.get_maps(i,j).etiquet == "s":
                    print("\33[31m",self.get_maps(i,j).etiquet+"\33[37m" ,end=" ")
                    s = s+1
                if self.get_maps(i,j).etiquet == "g":
                    print("\33[32m",self.get_maps(i,j).etiquet+"\33[37m" ,end=" ")
                    g = g+1
                if self.get_maps(i,j).etiquet == "o":
                    print("\33[33m",self.get_maps(i,j).etiquet+"\33[37m" ,end=" ")
                    o = o+1
                if self.get_maps(i,j).etiquet == "*":
                    print("\33[37m",self.get_maps(i,j).etiquet+"\33[37m" ,end=" ")
            print()
        print("\33[31m s for Iris-versicolor : ",s,"\33[37m")
        print("\33[32m g for Iris-virginica : ",g,"\33[37m")
        print("\33[33m o for Iris-setosa : ",o,"\33[37m")
        

    def distance_vect(self,tab1,tab2):
        distance = 0.0
        for i in range(self.size):
            distance = distance + math.pow((tab1[i]-tab2[i]),2)
        return math.sqrt(distance)

    def trouve_bmu(self,vect):
        min = 100.0
        for index in range(len(self.maps)):
            distance = self.distance_vect(vect.x,self.maps[index].w)
            if distance == min:
                bmu.append(self.get_index(index))
            if distance < min:
                bmu  = []
                bmu.append(self.get_index(index))
                min = distance
        return bmu

    def aleatoir_bmu(self,bmu):
        return bmu[random.randint(0,len(bmu)-1)]

    def change_etiquet(self,bmu,vect):
        self.get_maps(bmu.ligne,bmu.colonne).etiquet = vect.id[8]
        
    def modifier_poids(self,vect,bmu,alpha,rayon):
        for i in range(max(0,bmu.ligne-rayon),min(bmu.ligne+rayon,self.row-1)+1):
            for j in range(max(0,bmu.colonne-rayon),min(bmu.colonne+rayon,self.col-1)+1):
                for k in range(self.size):
                    self.get_maps(i,j).w[k] = self.get_maps(i,j).w[k] + alpha * (vect.x[k] -self.get_maps(i,j).w[k])

    def apprentisage(self,base,iteration,alpha_initial):
        rayon = 3
        partie = int(iteration/rayon)
        for t in range(iteration):
            alpha = alpha_initial * (1 - (t/iteration))
            random.shuffle(base.vect)
            for vect in base.vect:
                bmu  = self.aleatoir_bmu(self.trouve_bmu(vect))
                self.change_etiquet(bmu,vect)
                self.modifier_poids(vect,bmu,alpha,rayon)
            if t == partie:
                rayon = 2
            if t == 2*partie:
                rayon = 1
                

        


    

