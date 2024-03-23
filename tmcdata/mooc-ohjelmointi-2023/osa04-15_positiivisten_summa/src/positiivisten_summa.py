# tee ratkaisu tänne
def positiivisten_summa(lista:list):

    summa = 0
    for alkio in lista:
        if alkio > 0:
            summa+= alkio
        
    return summa
if __name__ == "__main__":
    print("vastaus ", positiivisten_summa([1,2]))