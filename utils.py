def capitalize(text):
    """Pārveido pirmo burtu uz lielo.
    Args:
        text: teksts apstrādei
    Returns:
        str: teksts ar lielo sākumburtu
    Example:
        >>> capitalize("labdien")
        'Labdien'
    """
    return text.capitalize()

def truncate(text, max_len=20):
    """Apgriež un pievieno "...", ja teksts pārsniegts limits
    
    Args:
        text: apstrādājamais teksts
        max_len: maksimālais garums (noklusējums 20)
        
    Returns:
        str: apgriezts teksts ar trim punktiniem
        
    Example:
        >>> truncate("laba diena! šis ir testējums tralalala", 10)
        'laba diena...'
    """
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text

def count_words(text):
    """Saskaita vārdus tekstā.
    
    Args:
        text: virkne ar vārdiem   
    Returns:
        int: vārdu skaits
    Example:
        >>> count_words("Labdien trešdiena!")
        2
    """
    return len(text.split())

def clamp(num, low, high):
    """Ierobežo/pārveido vērtību diapazonā.
    
    Args:
        num: skaitlis, cik ierobežot
        low: minimālā robeža
        high: maksimālā robeža
        
    Returns:
        int vai float: ierobežotā vērtība
    Example:
        >>> clamp(15, 0, 10)
        10
    """
    return max(low, min(num, high))

def is_prime(num):
    """Pārbauda, vai skaitlis ir pirmskaitlis (atgriež bool).
    Args:
        num: vesels skaitlis    
    Returns:
        bool: True, ja ir pirmskaitlis
        
    Example:
        >>> is_prime(7)
        True
    """
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def factorial(n):
    """Aprēķina n! (ar validāciju: n >= 0).
    
    Args:
        n: naturāls skaitlis
    Returns:
        int: faktoriāls
    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("n nevar būt negatīvs")
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def total(numbers):
    """Saraksta summa (ar for, ne sum()).
    
    Args:
        numbers: skaitļu saraksts
    Returns:
        int vai float: summa   
    Example:
        >>> total([1, 2, 3])
        6
    """
    t = 0
    for n in numbers:
        t += n
    return t

def average(numbers):
    """Vidējais aritmetiskais.
    
    Args:
        numbers: skaitļu saraksts    
    Returns:
        float: vidējā vērtība  
    Example:
        >>> average([10, 20])
        15.0
    """
    return total(numbers) / len(numbers) if numbers else 0

# --- Demo ---
if __name__ == "__main__":
    testa_teksts = "laba diena! šis ir testējums tralala tralalalalala bla bla bla"
    saīsināts = truncate(testa_teksts, 10)
    skaists_teksts = capitalize(saīsināts)
    
    print(f"Clamp tests: {clamp(15, 0, 10)}")
    print(f"Truncate tests: {skaists_teksts}")
    print(f"Factorial tests: {factorial(5)}")