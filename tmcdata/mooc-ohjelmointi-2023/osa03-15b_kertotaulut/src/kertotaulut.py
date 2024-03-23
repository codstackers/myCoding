# Kirjoita ratkaisu tähän
luku = int(input("Anna luku: "))
i = 1
while luku >= i:
    o = 1
    while o <= luku:
        t = i * o
        print(f"{i} x {o} = {t}")
        o += 1
    i += 1