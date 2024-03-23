# Kirjoita ratkaisu tähän
sana = input("Anna sana: ")

toinen = sana[1]
toiseksiviim = sana[len(sana) - 2]

if toinen == toiseksiviim:
    print(f"Toinen ja toiseksi viimeinen kirjain on {toinen}")
else:    
    print("Toinen ja toiseksi viimeinen kirjain eroavat")