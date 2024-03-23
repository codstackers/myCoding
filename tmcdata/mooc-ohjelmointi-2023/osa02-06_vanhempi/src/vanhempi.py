# Kirjoita ratkaisu tähän
print("Henkilö 1: ")
nimi1 = input("Nimi: ")
ikä1 = int(input("ikä: "))

print("Henkilö 2: ")
nimi2 = input("Nimi: ")
ikä2 = int(input("ikä: "))

if ikä1 > ikä2:
    print(f"Vanhempi on {nimi1}")
elif ikä1 < ikä2:
    print(f"Vanhempi on {nimi2}")
else:
    print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja")
