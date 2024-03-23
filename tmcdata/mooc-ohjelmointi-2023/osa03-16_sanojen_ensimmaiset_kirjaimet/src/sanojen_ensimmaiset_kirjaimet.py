# Kirjoita ratkaisu tähän
lause = input("Anna lause")

print(lause[0])
i = 1
while i < len(lause):
    if (lause[i].isspace()) == True:
        print(lause[i+1])
    i += 1
