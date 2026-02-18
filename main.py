from game_logic import generate_secret, check_guess, is_game_over
from ui import get_player_guess, show_hint, show_game_over, ask_play_again

def play_round():
    """Viena spēles raunda loģika"""
    secret = generate_secret()
    attempts = 0
    max_attempts = 10
    
    print(f"\nEs iedomājos skaitli no 1 līdz 100. Tev ir {max_attempts} mēģinājumi!")

    while not is_game_over(attempts, max_attempts):
        print(f"Mēģinājums {attempts + 1}: ", end="")
        guess = get_player_guess()
        
        if guess is None:
            continue
            
        attempts += 1
        result = check_guess(guess, secret)
        
        if result == "correct":
            show_game_over(secret, attempts, won=True)
            return
        
        show_hint(result)

    # Ja mēģinājumi beigušies un nav bijis "correct"
    show_game_over(secret, attempts, won=False)

if __name__ == "__main__":
    print("Apsveicu, Jūs esat skaitļu minēšanas spēlē!😍")
    while True:
        play_round()
        if not ask_play_again():
            print("Paldies par spēli!🙌 Uz redzēšanos!")
            break