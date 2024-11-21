class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self.__syote = syote
        self.__sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        syote = int(self.__syote())
        self.__sovelluslogiikka.plus(syote)


class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.__syote = syote
        self.__sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        syote = int(self.__syote())
        self.__sovelluslogiikka.miinus(syote)
    

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.__sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.__sovelluslogiikka.nollaa()


class Kumoa:
    def __init__(self, sovelluslogiikka, syote):
        pass

    def suorita(self):
        print("kumoa")