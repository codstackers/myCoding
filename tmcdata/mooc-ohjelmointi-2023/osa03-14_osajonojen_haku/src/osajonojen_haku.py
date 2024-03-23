# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")
tarkistus = ""
i = 0
while i < len(sana):
    tarkistus = sana[i]
    if tarkistus == merkki:
        if i + 3 <= len(sana):
            print(sana[i:i + 3])
    i += 1

