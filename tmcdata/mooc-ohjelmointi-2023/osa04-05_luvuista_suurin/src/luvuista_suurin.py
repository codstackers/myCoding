# tee ratkaisu tänne
def luvuista_suurin(a, b, c):

    if a <= b and b <= c:
        return c

    if b <= a and a <= c:
        return c

    if a <= c and c <= b:
        return b

    if c <= a and a <= b:
        return b

    if c <= b and b <= a:
        return a

    if b <= c and c <= a:
        return a


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(5, 5, 8)
    print(suurin)

    suurin = luvuista_suurin(11, 11, 11)
    print(suurin)

    suurin = luvuista_suurin(-20, -256, 0)
    print(suurin)