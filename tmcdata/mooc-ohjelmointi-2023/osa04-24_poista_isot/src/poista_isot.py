# tee ratkaisu tänne
def poista_isot(lista: list):
    lista2 = []
    for sana in lista:
        on_iso = sana.isupper()
        if on_iso != True:
            lista2.append(sana)
    return lista2
if __name__ == "__main__":
    print(poista_isot(["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]))