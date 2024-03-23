# tee ratkaisu tänne
def summa(lista1:list, lista2:list):

    uusi = []

    for i in range(len(lista1)):
        summa = lista1[i]+lista2[i]
        uusi.append(summa)
    return uusi
if __name__ == "__main__":
    tulos = summa([1,3,6], [9,6,2])
    print(tulos)