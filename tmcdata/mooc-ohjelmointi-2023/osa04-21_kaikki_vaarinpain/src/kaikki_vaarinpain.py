# tee ratkaisu tänne
def kaikki_vaarinpain(lista: list):
    lista2 = []
    for alkio in lista:
        lista2.insert(0, alkio[::-1])
    return lista2
if __name__ == "__main__":
    print(kaikki_vaarinpain(["Moi", "kaikki", "esimerkki", "vielä yksi"]))