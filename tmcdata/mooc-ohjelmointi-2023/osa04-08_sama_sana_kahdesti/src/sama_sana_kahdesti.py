# Kirjoita ratkaisu tähän
lista = []
i = 0
while True:
    sana = input("sana: ")
    if sana in lista:
        break
    lista.append(sana)
    i+= 1
print(f"Annoit {i} eri sanaa") 
