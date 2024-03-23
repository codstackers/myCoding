# tee ratkaisu tänne
def lista_tahtina(luvut: list):
    for i in range(len(luvut)):
        print(luvut[i]*"*")

if __name__ == "__main__":
    a = [3, 6, 8, 1, 5]
    lista_tahtina(a)