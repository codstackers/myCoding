# Kirjoita ratkaisu tähän
lista = []

while True:
    print(f"Lista on nyt {lista}")
    action = input("(l)isää, (p)oista vai e(x)it: ")

    if action == "l":
        if len(lista) == 0:
            lista.append(1)
        else:
            lista.append(lista[len(lista)-1]+1)

    if action == "p":
        if len(lista) == 0:
            print("Poistoa ei voida suorittaa koska lista on tyhjä!")
            continue
        else:
            lista.pop(len(lista)-1)

    if action == "x":
        print("Moi!")
        break

    else:
        continue
