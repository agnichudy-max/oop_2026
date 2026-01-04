class Pojazd:
    def jedz(self):
        print("Jade...")
    def hamuj(self):
        print("Hamuje...")

class Samochod(Pojazd):
    def __init__(self, marka):
        self.marka = marka
        self.model = model

class Honda(Samochod):
    def __init__(self, model):
        super().__init__("Honda", model)



