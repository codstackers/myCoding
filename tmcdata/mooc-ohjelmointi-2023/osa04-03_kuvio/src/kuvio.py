# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen

def viiva(numero, merkki):

    i = 0
    viiva = ""
    while i < numero:
        if merkki == "":
            print(numero * "*")
            break
        else:
            viiva += (merkki[0])
        i += 1
    if merkki != "":
        print(viiva)

def kuvio(kolmio, rivit1, pohja, rivit2):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 1
    while i <= kolmio:
        viiva(i, rivit1)
        i += 1
    e=0
    while e < pohja:
        viiva(kolmio, rivit2)
        e += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "x", 2, "o")
