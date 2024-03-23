# Kirjoita ratkaisu tähän
x = int(input("Lahjan suuruus? "))

if x < 5000:
    print(f"Vero: Ei veroa!")
if x >= 5000 and x < 25000:
    print(f"Vero: {100 + (x - 5000) * 0.08}")
if x >= 25000 and x < 55000:
    print(f"Vero: {1700 + (x - 25000) * 0.10}")
if x >= 55000 and x < 200000:
    print(f"Vero: {4700 + (x - 55000) * 0.12}")
if x >= 200000 and x < 1000000:
    print(f"Vero: {22100 + (x - 200000) * 0.15}")
if x >= 1000000:
    print(f"Vero: {142100 + (x - 1000000) * 0.17}")