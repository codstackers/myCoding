# tee ratkaisu tänne
def uniikit(lista:list):
    uusi = []
    for alkio in lista:
        if alkio in uusi:
            continue
        else:
            uusi.append(alkio)
    return sorted(uusi)

if __name__ == "__main__":
    print(uniikit([6,1,4,3,1,1,1,2,2,2,2,3,2,1,3,4,5,6,6,5,4,3,2,1,2]))

