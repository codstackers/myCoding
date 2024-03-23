# tee ratkaisu tänne
def parilliset(lista:list):

    uusi_lista = []

    for alkio in lista:
        if alkio != 0 and alkio % 2 == 0:
            uusi_lista.append(alkio)
    return uusi_lista
    print("alkuperäinen ", lista)
    print("uusi ", uusi_lista)
if __name__ == "__main__":
    parilliset([9, 7, -2, 0, -6,-3,-2,-8,-9,-5,-6,-4,0,1,2,3,4,5,6,7,8,9,])