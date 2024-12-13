from kivi_paperi_sakset import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto = None):
        return input("Toisen pelaajan siirto: ")
