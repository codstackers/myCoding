# tee ratkaisu tänne
def lyhin(lista:list):

    lyhin_nimi = len(lista[0])
    nimi = ""

    for merkkijono in lista:
        if len(merkkijono) < lyhin_nimi:
            lyhin_nimi = len(merkkijono)
            nimi = merkkijono
    return nimi

if __name__ == "__main__":
    print(lyhin(["aki", "pekka", "emilia", "venla", "eero", "antti", "b", "a"]))
