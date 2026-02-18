def get_player_guess():
    """Pieprasa un validē ievadi (atgriež int vai None)
    
    Atgriež:
        int vai None: Skaitlis, ja derīgs, pretējā gadījumā None
    """
    ievade = input("Tavs minējums? ")
    if not ievade.isnumeric():
        print("❌ Lūdzu, ievadi ciparu!")
        return None
    return int(ievade)

def show_hint(result):
    """Parāda padomu"""
    if result == "too_low":
        print("Par mazu! Pamēģini lielāku.")
    elif result == "too_high":
        print("Par lielu! Pamēģini mazāku.")

def show_game_over(secret, attempts, won):
    """Beigu ziņojums
    
    Args:
        secret: Pareizais skaitlis
        attempts: Izmantotie mēģinājumi
        won: Vai lietotājs uzvarēja (bool)
    """
    if won:
        print(f"APSVEICU! 💕Tu uzminēji {secret} ar {attempts}. mēģinājumu!")
    else:
        print(f"Diemžēl mēģinājumi beidzās😢 Mans skaitlis bija {secret}.")

def ask_play_again():
    """Vai spēlēt vēlreiz
    
    Returns:
        bool: True, ja vēlas turpināt
    """
    velreiz = input("\nVai vēlies spēlēt vēlreiz? (jā/nē): ").lower()
    return velreiz.startswith('j')

if __name__ == "__main__":
    # Testa piemēri 
    show_hint("too_high")
    show_game_over(42, 5, won=True)