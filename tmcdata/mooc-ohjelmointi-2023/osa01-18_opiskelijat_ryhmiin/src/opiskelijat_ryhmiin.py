# Kirjoita ratkaisu tähän
opMäärä = int(input("Montako opiskelijaa? "))
ryhmöKoko = int(input("Mikä on ryhmän koko? "))

ryhmienMäärä = (opMäärä // ryhmöKoko)
jako = (opMäärä / ryhmöKoko)
ryhmienMäärä1 = ryhmienMäärä + 1
if ryhmienMäärä == jako:
    print(f"Ryhmien määrä: {ryhmienMäärä}")    
else:
    print(f"Ryhmien määrä: {ryhmienMäärä1}")