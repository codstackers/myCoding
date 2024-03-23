# tee ratkaisu tänne
def pisimmat(lista:list):

    pisin = 0
    uusi = []

    for merkkijono in lista:
        if len(merkkijono) > pisin:
            pisin = len(merkkijono)

    for pisimmat_nimet in lista:
        if len(pisimmat_nimet) == pisin:
            uusi.append(pisimmat_nimet)
    return uusi

if __name__ == "__main__":
    print(pisimmat(["pekka", "emilia", "venla", "eero", "antti", "juhani"]))
