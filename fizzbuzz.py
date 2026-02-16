import sys

# 1. SOLIS: Dabūjam skaitli N
# Ja neesi ierakstījusi skaitli terminālī (python fizzbuzz.py 15), 
# programma to paprasīs ar input(). Tā kods "nenobruks".
if len(sys.argv) < 2:
    ievade = input("Cik tālu skaitīsim? Ierakstīt skaitli: ")
else:
    ievade = sys.argv[1]

# 2. SOLIS: Mēģinām pārvērst ievadi par skaitli un sākt skaitīšanu
try:
    n = int(ievade)
    
    # Range(1, n + 1) nodrošina, ka sāk no 1 un aiziet līdz pašam N
    for i in range(1, n + 1):
        vārds = ""
        
        # Pārbaudām dalāmību (atlikums % ir 0)
        if i % 3 == 0:
            vārds += "Fizz"
        if i % 5 == 0:
            vārds += "Buzz"
        if i % 7 == 0:  # Bonuss: Jazz
            vārds += "Jazz"
            
        # Ja kabatiņa 'vārds' ir tukša, izvada pašu skaitli
        if vārds == "":
            print(i, end="")
        else:
            print(vārds, end="")
            
        # Pieliek komatu smukumam, ja tas nav pēdējais skaitlis
        if i < n:
            print(", ", end="")
            
    print("\n Gatavs!")

except ValueError:
    print("❌ Kļūda: Lūdzu, ievadi tikai veselu skaitli!")
