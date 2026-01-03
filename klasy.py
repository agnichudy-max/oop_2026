#Klasa
#Istota
#Zamysl

class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
        self.imie = imie
        print(f"Niech powstanie Czlowiek o imieniu {imie}")

#powstanie obiektu / gotowanie z przepisu
adam = Czlowiek("Adam") #a = 4 # a = int(4)
ewa = Czlowiek("Ewa")
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)

#print(type(adam))
#print(dir(Czlowiek))
#print(dir(adam))


