# kopioi edellisestä tehtävästä funktion viiva koodi tänne
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

def risunelio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 0
    while i < koko:
        viiva(koko, "#")
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(10)
