# Tee ratkaisu tänne
def anagrammi(sana1, sana2):
    if sorted(sana1) == sorted(sana2):
        return True
    return False

if __name__ == "__main__":
    print(anagrammi("olat", "talo"))
