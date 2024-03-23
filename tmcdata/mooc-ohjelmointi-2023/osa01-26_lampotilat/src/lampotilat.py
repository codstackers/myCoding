# Kirjoita ratkaisu tähän
temp = int(input("Anna lämpötila (F): "))

c = float(temp - 32) * 5 / 9

if c < 0:
    print(f"{temp} fahrenheit-astetta on {c} celsius-astetta")
    print("Paleltaa!")
if c >= 0:
    print(f"{temp} fahrenheit-astetta on {c} celsius-astetta")