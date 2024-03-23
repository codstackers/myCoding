# tee ratkaisu tänne
def samat(sana, num1, num2):

    if num1 >= len(sana) or num2 >= len(sana):
        return False

    if sana[num1] == sana[num2]:
        return True
    else: 
        return False

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 12)) 