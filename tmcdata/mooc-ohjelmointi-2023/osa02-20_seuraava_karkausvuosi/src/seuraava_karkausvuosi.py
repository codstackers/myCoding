# Kirjoita ratkaisu tähän
vuosi = int(input("Vuosi: "))
org = vuosi
kierros = 0

while True:
    karkaus = False

    if vuosi < 100:
        if vuosi % 4 == 0:
            karkaus = True


    if vuosi >= 400:
        if vuosi % 4 == 0 and vuosi % 100 != 0:
            karkaus = True
        if vuosi % 4 == 0 and vuosi % 100 == 0 and vuosi % 400 == 0:
            karkaus = True

    kierros += 1
    if karkaus == True and kierros != 1:
            break
    else:
        vuosi += 1

print(f"Vuotta {org} seuraava karkausvuosi on {vuosi}")                