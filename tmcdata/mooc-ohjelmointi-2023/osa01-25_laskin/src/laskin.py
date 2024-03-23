# Kirjoita ratkaisu tähän
luku1 = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))
komento = input("Komento: ")

s = luku1 + luku2
t = luku1 * luku2
e = luku1 - luku2

if komento == "summa":
    print(f"{luku1} + {luku2} = {s}")
if komento == "tulo":
    print(f"{luku1} * {luku2} = {t}")
if komento == "erotus":
    print(f"{luku1} - {luku2} = {e}")


