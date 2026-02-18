import random

def generate_secret(low=1, high=100):
    """Ģenerē nejaušu skaitli norādītajā diapazonā.
    
    Args:
        low: Zemākā robeža
        high: Augstākā robeža
    Returns:
        int: Nejaušs skaitlis
    """
    return random.randint(low, high)

def check_guess(guess, secret):
    """Salīdzina minējumu ar noslēpumu un atgriež rezultāta kodu.
    
    Args:
        guess: Lietotāja skaitlis
        secret: Datora skaitlis
    Returns:
        str: "correct", "too_high" vai "too_low"
    """
    if guess == secret:
        return "correct"
    elif guess > secret:
        return "too_high"
    else:
        return "too_low"

def is_game_over(attempts, max_attempts=10):
    """Pārbauda, vai mēģinājumu skaits ir izsmelts.
    
    Args:
        attempts: Pašreizējais mēģinājumu skaits
        max_attempts: Maksimāli pieļaujamais skaits
    Returns:
        bool: True, ja spēle beigusies
    """
    return attempts >= max_attempts

if __name__ == "__main__":
    # Testa piemēri loģikai
    print(f"Loģikas tests (50 vs 100): {check_guess(50, 100)}")
    print(f"Spēles beigu tests (10/10): {is_game_over(10, 10)}")