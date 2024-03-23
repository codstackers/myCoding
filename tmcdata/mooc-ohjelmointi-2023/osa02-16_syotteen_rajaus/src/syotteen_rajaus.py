from math import sqrt
# Kirjoita ratkaisu tähän
while True:
    luku = int(input("Syötä luku: "))
    if  luku < 0:
        print("Epäkelpo luku ")
    if luku > 0:
        print((sqrt(luku)))
    else:
        break
print("Lopetetaan...")