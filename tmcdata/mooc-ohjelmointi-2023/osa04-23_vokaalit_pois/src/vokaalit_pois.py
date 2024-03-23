# tee ratkaisu tänne
def ilman_vokaaleja(mjono: str):
    vokaalit = "aeiouyåäö"
    i = 0
    while i < len(vokaalit):
        for kirjain in mjono:
            mjono = mjono.replace(vokaalit[i], "")
        i+= 1
    return mjono
if __name__ == "__main__":
    print(ilman_vokaaleja("mouyoiaåöjlkdciodfoijdsfeqwopiäikka"))