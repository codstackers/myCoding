# Kirjoita ratkaisu tähän
a = input("Anna 1. kirjain: ")
b = input("Anna 2. kirjain: ")
c = input("Anna 3. kirjain: ")

if a <= b and b <= c:
    print(f"Keskimmäinen kirjain on {b}")

if b <= a and a <= c:
    print(f"Keskimmäinen kirjain on {a}")

if a <= c and c <= b:
    print(f"Keskimmäinen kirjain on {c}")

if c <= a and a <= b:
    print(f"Keskimmäinen kirjain on {a}")

if c <= b and b <= a:
    print(f"Keskimmäinen kirjain on {b}")

if b <= c and c <= a:
    print(f"Keskimmäinen kirjain on {c}")
