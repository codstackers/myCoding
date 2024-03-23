# Kirjoita ratkaisu tähän
kertaaViikossa = int(input("Montako kertaa viikossa syöt Unicafessa? "))
lounaanHinta = float(input("Unicafe-lounaan hinta? "))
muuRuoka = float(input("Paljonko käytät viikossa ruokaostoksiin? "))

viikossa = float(kertaaViikossa * lounaanHinta + muuRuoka)
päivässä = float(viikossa / 7)

print("Kustannukset keskimäärin:")
print(f"Päivässä {päivässä} euroa")
print(f"Viikossa {viikossa} euroa")