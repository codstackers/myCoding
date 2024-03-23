# Kirjoita ratkaisu tähän
while True:
    luku = int(input("Anna luku: "))
    org = luku
    if luku <= 0:
        print("Kiitos ja moi!")
        break
    lopputulos = 1
    while luku > 0:
        lopputulos *= luku
        luku -= 1
    print(f"Luvun {org} kertoma on {lopputulos}")
