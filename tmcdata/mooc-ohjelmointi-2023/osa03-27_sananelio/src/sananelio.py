# tee ratkaisu tänne
def nelio(sana, kerta):
    putkeen = (sana*kerta*kerta)
    i = 0
    siirto = 0
    while i < kerta:
        print(putkeen[siirto:siirto+kerta])
        i += 1
        siirto += kerta
if __name__ == "__main__":
    nelio("python", 15)