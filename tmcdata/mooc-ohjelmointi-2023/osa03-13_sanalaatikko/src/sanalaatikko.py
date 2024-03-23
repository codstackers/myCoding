# Kirjoita ratkaisu tähän
sana = input("Sana: ")
sivut = int((28 - len(sana)) / 2)

print("*" * 30)
if len(sana) % 2 != 0:
    print("*" + " " * sivut + sana + " " * (sivut + 1) + "*")
else:
    print("*" + " " * sivut + sana + " " * sivut + "*")    
print("*" * 30)
