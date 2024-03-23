# Kirjoita ratkaisu tähän
luku = int(input("Anna luku: "))

neg = luku * -1
if luku < 0:
    print(f"Luvun itseisarvo on {neg}")
if luku >= 0:
    print(f"Luvun itseisarvo on {luku}")