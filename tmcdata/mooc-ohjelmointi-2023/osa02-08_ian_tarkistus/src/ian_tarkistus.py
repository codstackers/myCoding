# Kirjoita ratkaisu tähän
ika = int(input("Kerro ikäsi: "))

if ika > 4 and ika < 101:
    print(f"Ok, olet siis {ika}-vuotias")
elif ika < 5 and ika >= 0:
    print("En usko, että osaat kirjoittaa...")
else:
    print("Taitaa olla virhe")