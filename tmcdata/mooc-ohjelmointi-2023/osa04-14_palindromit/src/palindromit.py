# tee ratkaisu tänne
def palindromi(sana:str):
        suora = []
        kaant = []
        for i in sana:
            suora.append(i)
            kaant.insert(0, i)

        if suora == kaant:
            return True
        else: 
            return False

while True:
    sana = input("Anna palindromi: ")
    tulos = palindromi(sana)
    if tulos == True:
        print(f"{sana} on palindromi!")
        break

    else:
        print("ei ollut palindromi")

    


