# tee ratkaisu tänne
def eniten_kirjainta(mj: str):
    eniten = 0
    for kirjain in mj:
        lukema = mj.count(kirjain)
        if lukema > eniten:
            eniten = lukema
            eniten_esiintyva_kirjain = kirjain

    return eniten_esiintyva_kirjain
    
if __name__ == "__main__":
    print(eniten_kirjainta("mmmmmmooooookkki"))