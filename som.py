from base import Base
from network import Network

def main():
    base = Base("iris.data")
    base.remplire_vect()
    base.normalisation_base()

    network = Network(10,6,base.col,base.moyenne(),0.02)
   
    network.apprentisage(base,500,0.9)
    network.apprentisage(base,1500,0.09)
    network.affiche_network()

if __name__ == '__main__' :
    main()




