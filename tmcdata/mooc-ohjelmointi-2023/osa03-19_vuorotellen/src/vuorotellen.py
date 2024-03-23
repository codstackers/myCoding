# Kirjoita ratkaisu tähän
luku = int(input("Anna luku: "))
pariton = luku % 2 != 0
puolet = luku / 2
i = 1

while i <= puolet:
    print(i)
    print(luku)
    i += 1
    luku -= 1
if pariton == True:
    print(i)