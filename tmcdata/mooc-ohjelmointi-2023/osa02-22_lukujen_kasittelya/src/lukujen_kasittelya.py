# Kirjoita ratkaisu tähän
lukujaYhteensa = 0
summa = 0 
ka = 0
positiivinen = 0
negatiivinen = 0

print("Syötä kokonaislukuja, 0 lopettaa:")
while True:
    luku = int(input("Luku:"))
    if luku == 0:
        break
    lukujaYhteensa += 1
    summa += luku
    ka = summa / lukujaYhteensa
    if luku > 0:
        positiivinen += 1
    if luku < 0:
        negatiivinen += 1

print(f"Lukuja yhteensä {lukujaYhteensa}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {ka}")
print(f"Positiivisia {positiivinen}")
print(f"Negatiivisia {negatiivinen}")


