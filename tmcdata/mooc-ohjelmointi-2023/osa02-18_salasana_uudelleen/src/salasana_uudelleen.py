# Kirjoita ratkaisu tähän
ekaPw = input("Salasana: ")
tokaPw = input("Toista salasana: ")
while True:
    if ekaPw == tokaPw:
        break
    if ekaPw != tokaPw:
        print("Ei ollut sama!")
        tokaPw = input("Toista salasana: ")
print("Käyttäjätunnus luotu!")