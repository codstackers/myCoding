# Kirjoita ratkaisu tähän
while True:
    merkkij = input("Anna merkkijono:")
    mjPituus = len(merkkij)
    
    if mjPituus == 0:
        break
    else:
        print(merkkij)
        print("-" * mjPituus)