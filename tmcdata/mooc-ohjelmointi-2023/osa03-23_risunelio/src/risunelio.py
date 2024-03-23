# tee ratkaisu tänne

def risunelio(pituus):
    i = pituus
    while i > 0:
        print("#" * pituus)
        i -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
    risunelio(4)
    risunelio(8)