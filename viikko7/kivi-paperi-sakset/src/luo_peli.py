from kps_tekoaly import KPSTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli():
    vastaus = input()

    if vastaus == 'a':
        return KPSPelaajaVsPelaaja()
    if vastaus == 'b':
        return KPSTekoaly()
    if vastaus == 'c':
        return KPSParempiTekoaly()

    return None
