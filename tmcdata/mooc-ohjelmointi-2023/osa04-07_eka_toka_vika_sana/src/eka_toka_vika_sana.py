# tee ratkaisu tänne

def eka_sana(merkkijono):

    empty = " "
    i = 0
    while i < len(merkkijono) - 1:
        if merkkijono[i] == empty:
            return merkkijono[0:i]
            break
        i+= 1

def toka_sana(merkkijono):

    empty = " "
    i = 0
    toinen_sana = 0
    kerta = 0
    while i < len(merkkijono) - 1:
        if merkkijono[i] == empty:
            kerta+= 1
            if kerta == 1:
                toinen_sana = i
            if kerta > 1:
                return merkkijono[toinen_sana+1:i]
        if i == len(merkkijono) - 2:
            return merkkijono[toinen_sana+1:len(merkkijono)]

        i+= 1
    
def vika_sana(merkkijono):

    empty = " "
    i = 0
    viimesin = 0
    kerta = 0
    while i < len(merkkijono) - 1:
        if merkkijono[i] == empty:
            viimesin = i
        i+= 1
    return merkkijono[viimesin+1:len(merkkijono)]

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lause = "Lorem ipsum vaikka mitä"
    print(eka_sana(lause))
    print(toka_sana(lause)) 
    print(vika_sana(lause))