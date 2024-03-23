# Kirjoita ratkaisu tähän
merkkijono = input("Anna merkkijono: ")
maara = int(input("Anna määrä: "))
tulos = ""

while maara > 0:
    tulos += merkkijono
    maara -= 1
print(tulos)