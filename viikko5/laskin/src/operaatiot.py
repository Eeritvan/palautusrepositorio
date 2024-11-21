class Summa:
    def __init__(self, sovelluslogiikka, syote):
        self._syote = syote
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_tila = 0

    def suorita(self):
        syote = int(self._syote())
        self._edellinen_tila = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.plus(syote)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_tila)


class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self._syote = syote
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_tila = 0

    def suorita(self):
        syote = int(self._syote())
        self._edellinen_tila = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.miinus(syote)
    
    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_tila)


class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_tila = 0

    def suorita(self):
        self._edellinen_tila = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_tila)


class Kumoa:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._viimeisin_komento = None

    def aseta_viimeisin_komento(self, komento):
        self._viimeisin_komento = komento

    def suorita(self):
        if self._viimeisin_komento:
            self._viimeisin_komento.kumoa()