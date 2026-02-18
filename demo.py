from utils import capitalize, clamp, is_prime, average, factorial
from validators import is_email, is_strong_password, is_valid_date

def run_demonstration():
    """Demonstrē funkcijas no utils.py un validators.py."""
    
    print("=== Utils demonstrācija ===")
    # 1. Capitalize
    print(f"capitalize('hello') -> '{capitalize('hello')}'")
    
    # 2. Clamp
    print(f"clamp(15, 0, 10) -> {clamp(15, 0, 10)}")
    
    # 3. Is Prime
    print(f"is_prime(17) -> {is_prime(17)}")
    
    # 4. Average
    print(f"average([10, 20, 30]) -> {average([10, 20, 30])}")
    
    # 5. Factorial ar kļūdu apstrādi (try/except)
    try:
        print(f"factorial(-1) -> ", end="")
        print(factorial(-1))
    except ValueError as e:
        print(f"ValueError: {e}")

    print("\n=== Validators demonstrācija ===")
    # 6. Email
    print(f"is_email('test@test.lv') -> {is_email('test@test.lv')}")
    
    # 7. Password
    print(f"is_strong_password('abc') -> {is_strong_password('abc')}")
    
    # 8. Date
    print(f"is_valid_date('2025-13-01') -> {is_valid_date('2025-13-01')}")

if __name__ == "__main__":
    run_demonstration()