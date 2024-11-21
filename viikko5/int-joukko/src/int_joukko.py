KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or not isinstance(kasvatuskoko, int):
            raise ValueError("kapasiteetti and kasvatuskoko must be integers")
        if kapasiteetti < 0 or kasvatuskoko < 0:
            raise ValueError("kapasiteetti and kasvatuskoko must be non-negative")
        
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.kokolista = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.kokolista

    def lisaa(self, luku: int):
        if not self.kuuluu(luku):
            self.kokolista[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.kokolista):
                taulukko_old = self.kokolista
                self.kokolista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.kokolista)

    def poista(self, luku: int):
        try:
            kohta = self.kokolista.index(luku)
            self.kokolista.pop(kohta)
            self.alkioiden_lkm -= 1
        except:
            return

    def kopioi_lista(self, a: list, b: list):
        b[:len(a)] = a

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.kokolista[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a: list, b: list):
        uusi_lista = IntJoukko()
        lista_a = a.to_int_list()
        lista_b = b.to_int_list()

        for luku in lista_a + lista_b:
            uusi_lista.lisaa(luku)

        return uusi_lista

    @staticmethod
    def leikkaus(a: list, b: list):
        uusi_lista = IntJoukko()
        lista_a = a.to_int_list()
        lista_b = b.to_int_list()

        for luku in lista_a:
            if luku in lista_b:
                uusi_lista.lisaa(luku)

        return uusi_lista

    @staticmethod
    def erotus(a: list, b: list):
        uusi_lista = IntJoukko()
        lista_a = a.to_int_list()
        lista_b = b.to_int_list()

        for luku in lista_a:
            if luku not in lista_b:
                uusi_lista.lisaa(luku)

        return uusi_lista

    def __str__(self):
        return "{" + ", ".join(map(str, self.kokolista[:self.alkioiden_lkm])) + "}"
