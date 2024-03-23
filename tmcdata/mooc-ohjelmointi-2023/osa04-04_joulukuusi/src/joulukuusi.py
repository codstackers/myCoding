# tee ratkaisu tänne

def joulukuusi(koko):
    print("joulukuusi!")
    sivut = koko - 1
    i = 1
    e = 0

    while e < koko:
        rivi = ((sivut * " " ) +  (i * "*") + (sivut * " "))
        print(rivi)
        i += 2
        e += 1
        sivut -= 1
    
    print(((koko -1) * " ") + (1 * "*") + ((koko -1) * " "))


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(5)
    joulukuusi(15)
    joulukuusi(35)
    joulukuusi(45)
    joulukuusi(50)
    