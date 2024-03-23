# tee ratkaisu tänne
def pisimman_pituus(lista:list):

    pisin = 0

    for merkkijono in lista:
        if len(merkkijono) > pisin:
            pisin = len(merkkijono) 
    return pisin

if __name__ == "__main__":
    print(pisimman_pituus(["pekka", "emilia", "venla", "eeeeeeero", "antti", "juhani"]))
