#Klasa
#Istota
#Zamysl
from zipfile import sizeEndCentDir


class Czlowiek:
    gatunek = "Homo Sapiens"
    def __init__(self, imie, plec):
        self.imie = imie
        self.plec = plec

        print(f"Niech powstanie Czlowiek o imieniu {imie}")

    # Metoda - funkcja w ramach klasy

    def przedstaw_sie(self):
        print(f"Dzień dobry mam na inie {self.imie} i jestem ", end="")
        if self.plec == "M":
            print ("mezczyzną")
        else:
            print ("kobietą")



    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")
class Dziecko(Czlowiek):
   def Baw_sie(self):
       print(("Ale zabawa"))
   def przedstaw_sie(self):
       print(f"czesc, jestem {self.imie} i jestem ", end="")
       if self.plec == "M":
           print("chlopcem")
       else:
           print("dziewczynka")


#powstanie obiektu / gotowanie z przepisu
adam = Czlowiek("Adam", "M") #a = 4 # a = int(4)
ewa = Czlowiek("Ewa", "K")
agnieszka = Czlowiek("Agnieszka", "K")
ewa.przedstaw(adam)
adam.przedstaw_sie()
kain = Dziecko("Kain", "M")
kain.Baw_sie()

kain.przedstaw_sie()







# print(adam.imie)
# print(ewa.imie)
# print(agnieszka.imie)
#print(type(adam))
#print(dir(Czlowiek))
#print(dir(adam))


