# Kirjoita ratkaisu tähän
vuosi = int(input("Anna vuosi: "))

if vuosi > 0 and vuosi < 100:
    if vuosi % 4 == 0:
        print("Vuosi on karkausvuosi")
    else:
        print("Vuosi ei ole karkausvuosi.")
elif vuosi >= 100:     
    if vuosi % 100 == 0 and vuosi % 400 != 0:
        print("Vuosi ei ole karkausvuosi.")
    elif vuosi % 4 == 0:
        print("Vuosi on karkausvuosi")
    else:
        print("Vuosi ei ole karkausvuosi.")
