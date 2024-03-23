# Kirjoita ratkaisu tähän
j1 = input("Anna jono 1: ")
j2 = input("Anna jono 2: ")

jono1 = len(j1)
jono2 = len(j2)

if jono1 > jono2:
    print(f"{j1} on pidempi")
elif jono1 < jono2:
    print(f"{j2} on pidempi")
else:
    print(f"Jonot ovat yhtä pitkät")
    

