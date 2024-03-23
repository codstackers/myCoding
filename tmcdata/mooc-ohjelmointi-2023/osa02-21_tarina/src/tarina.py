# Kirjoita ratkaisu tähän
lause = ""
edellinen = ""

while True:
    sana = input("Anna sana: ")
    if sana == "loppu" or sana == edellinen:
        break
    else:
        lause += sana + " "
        edellinen = sana
print(lause)
