def is_email(text):
    """Epasta validācija (satur @ un .)."""
    return "@" in text and "." in text

def is_phone_number(text):
    """LV formāts: +371 XXXXXXXX (kopā 8 cipari pēc koda)."""
    if text.startswith("+371 ") and len(text.replace(" ", "")) == 12:
        return text.replace("+371 ", "").isdigit()
    return False

def is_valid_age(age):
    """Pārbauda, vecumu robežās 0-150."""
    try:
        a = int(age)
        return 0 <= a <= 150
    except:
        return False

def is_strong_password(text):
    """Vismaz 8 simboli, satur burtus UN ciparus."""
    if len(text) < 8:
        return False
    has_letter = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)
    return has_letter and has_digit

def is_valid_date(text):
    """Pārbauda YYYY-MM-DD formātu un loģiskās vērtības.
    
    Args:
        text: datums teksta formātā
        
    Returns:
        bool: True, ja datums ir pareizs, citādi False
    """
    parts = text.split("-")
    
    # Pārbauda, vai ir 3 daļas un vai tās ir cipari
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        
        # PIEVIENOTĀ PĀRBAUDE:
        if year > 0 and 1 <= month <= 12 and 1 <= day <= 31:
            return True
            
    return False

# --- Demo ---
if __name__ == "__main__":
    print("--- E-pasta testi ---")
    print(f"is_email('anna@inbox.lv') -> {is_email('anna@inbox.lv')}") # True
    print(f"is_email('anna') -> {is_email('anna')}")                 # False
    print(f"is_email('anna@') -> {is_email('anna@')}")               # False

    print("\n--- Telefona numura testi ---")
    print(f"is_phone_number('+371 26123456') -> {is_phone_number('+371 26123456')}") # True
    print(f"is_phone_number('26123456') -> {is_phone_number('26123456')}")           # False

    print("\n--- Vecuma testi ---")
    print(f"is_valid_age(25) -> {is_valid_age(25)}")   # True
    print(f"is_valid_age(200) -> {is_valid_age(200)}") # False
    print(f"is_valid_age('abc') -> {is_valid_age('abc')}") # False