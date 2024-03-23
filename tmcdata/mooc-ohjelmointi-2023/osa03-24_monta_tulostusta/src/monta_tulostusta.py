# tee ratkaisu tähän

def tulosta_monesti(merkkijono, kertaa):
    while kertaa > 0:
        print(merkkijono)
        kertaa -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    tulosta_monesti("python", 5)
    tulosta_monesti("Mitä mitää..", 3)