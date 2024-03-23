# Kirjoita ratkaisu tähän
yritykset = 0

while True:
    pin = input("PIN-koodi: ")
    yritykset += 1

    if pin == "4321":
        break
    else:
        print("Väärin")

if yritykset == 1:
    print(f"Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {yritykset} yritystä")