class Auto:
    def __init__(self):
        self.silnik = None
        self.kola = None
        self.karoseria = None
    def __str__(self):
        return f" Auto z silnikiem: {self.silnik},\n kołami: {self.kola},\n karoserią: {self.karoseria}"

class InzynierSamochodowy:
    def wstaw_silnik(self): pass
    def wstaw_kola(self): pass
    def maluj_karoserie(self): pass
    def zwroc_auto(self): pass

class InzynierAutSportowych(InzynierSamochodowy):
    def __init__(self):
        self.auto = Auto()
    def wstaw_silnik(self):
        self.auto.silnik = "Silnik V8"
    def wstaw_kola(self):
        self.auto.kola = "Koła sportowe"
    def maluj_karoserie(self):
        self.auto.karoseria = "Czerwona"
    def zwroc_auto(self):
        return self.auto

class Kierownik:
    def __init__(self, robotnik: InzynierSamochodowy):
        self.robotnik = robotnik
    def zbuduj_auto(self):
        self.robotnik.wstaw_silnik()
        self.robotnik.wstaw_kola()
        self.robotnik.maluj_karoserie()
        return self.robotnik.zwroc_auto()

if __name__ == "__main__":
    mariusz = InzynierAutSportowych()
    kierownik = Kierownik(mariusz)
    sportowe_auto = kierownik.zbuduj_auto()
    print(sportowe_auto)
