# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")

indexi = sana.find(merkki)
oikea = indexi + 3

if oikea <= len(sana):
    print(sana[indexi:oikea])