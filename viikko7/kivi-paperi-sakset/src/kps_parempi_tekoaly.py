from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__ (self):
        self._parannettu_tekoaly = TekoalyParannettu(10)
    
    def _toisen_siirto(self, ensimmaisen_siirto = None):
        siirto = self._parannettu_tekoaly.anna_siirto()
        self._parannettu_tekoaly.aseta_siirto(ensimmaisen_siirto)
        print(f"Tietokone valitsi: {siirto}")
        return siirto
