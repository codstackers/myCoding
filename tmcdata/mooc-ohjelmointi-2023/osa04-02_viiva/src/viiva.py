# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
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

if __name__ == "__main__":
    viiva(5, "x")
    viiva(10, "LOLx")
    viiva(15, "%/€&x")
    viiva(15, "€&x")
    viiva(15, "")
