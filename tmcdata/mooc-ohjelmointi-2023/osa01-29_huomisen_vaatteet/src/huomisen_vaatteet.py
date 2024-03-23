# Kirjoita ratkaisu tähän
# Kirjoita ratkaisu tähän
print("Kerro huominen sääennuste: ")
temp = int(input("Lämpötila: "))
rain = (input("Sataako (kyllä/ei): "))

if temp < 100:
    print("Pue housut ja t-paita")
if temp < 21:
    print("Ota myös pitkähihainen paita")
if temp < 11:
    print("Pue päälle takki")
if temp < 6:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")

if rain == "kyllä":
    print("Muista sateenvarjo!")