# Kirjoita ratkaisu tähän
asti = int(input("Mihin asti: "))
luku = 1
summa = 0
plus = " + "
laskettiin = "1"
while summa < asti:
    summa += luku
    if luku > 1:
        laskettiin += plus + str(luku)
    luku += 1
print(f"Laskettiin {laskettiin} = {summa}")