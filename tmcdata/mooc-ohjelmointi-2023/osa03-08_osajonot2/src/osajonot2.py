# Kirjoita ratkaisu tähän
mj = input("Anna merkkijono: ")
n = 1
viimeinen = len(mj)
while n <= viimeinen:
    print(mj[viimeinen - n:viimeinen])
    n += 1
