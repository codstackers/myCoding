# Kirjoita ratkaisu tähän
alkiot = int(input("Kuinka monta lukua: "))
lista = []
i = 0
while i < alkiot:
    i+= 1
    luku = int(input(f"Anna luku {i}: "))
    lista.append(luku)
print(lista)