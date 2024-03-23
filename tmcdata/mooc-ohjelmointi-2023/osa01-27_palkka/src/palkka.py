# Kirjoita ratkaisu tähän
tuntipalkka = float(input("Tuntipalkka: "))
tunnit = int(input("Työtunnit: "))
päivä = input("Viikonpäivä: ")

palkka = float(tuntipalkka * tunnit)
sunn = palkka * 2

if päivä == "sunnuntai":
    print(f"Palkka {sunn} euroa")
if päivä != "sunnuntai":
    print(f"Palkka {palkka} euroa")