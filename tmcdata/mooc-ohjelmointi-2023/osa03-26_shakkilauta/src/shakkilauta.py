# tee ratkaisu tänne
def shakkilauta(rivit):
    leveys = rivit 
    i = 1
    
    while i <= rivit:
        if i % 2 != 0:
            ruutu = 1
            neliot = ""
            while ruutu <= leveys:
                if ruutu % 2 != 0:
                    neliot += "1"
                else:
                    neliot += "0"
                ruutu += 1
            print(neliot) 
        else:
            ruutu = 0
            neliot = ""
            while ruutu < leveys:
                if ruutu % 2 != 0:
                    neliot += "1"
                else:
                    neliot += "0"
                ruutu += 1
            print(neliot)     
        i += 1
# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(9)
