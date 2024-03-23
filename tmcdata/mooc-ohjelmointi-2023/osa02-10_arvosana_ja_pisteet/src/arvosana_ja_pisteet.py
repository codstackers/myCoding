# Kirjoita ratkaisu tähän
pisteet = int(input("Anna pisteet [0-100]: "))

if pisteet >= 0 and pisteet <= 49:
    arvosana = "hylätty"
elif pisteet > 49 and pisteet <= 59:
    arvosana = "1"
elif pisteet > 59 and pisteet <= 69:
    arvosana = "2"
elif pisteet > 69 and pisteet <= 79:
    arvosana = "3"
elif pisteet > 79 and pisteet <= 89:
    arvosana = "4"
elif pisteet > 89 and pisteet <= 100:
    arvosana = "5"
else:
    arvosana = "mahdotonta!"

print("Arvosana: " + arvosana)


