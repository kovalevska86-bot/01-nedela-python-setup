# --- Mani pirmie soļi Python ---

# 1. Izveidoju divus jaukus mainīgos
mans_hobijs = "Joga"      # Šis ir teksts jeb 'str'
kafijas_tases = 2         # Šis ir vesels skaitlis jeb 'int'

# 2. Pārbaudu, kādus tipus Python tiem ir piešķīris
print("Hobija tips:")
print(type(mans_hobijs))

print("Kafijas tasīšu tips:")
print(type(kafijas_tases))

# 3. Trīs pārbaudes: vai šīs lietas Python acīs ir "patiesas" (True/False)?
print("--- Truthy / Falsy pārbaudes ---")
print(bool("Ziedi"))    # True, jo teksts nav tukšs
print(bool(""))          # False, jo šī ir tukša rinda
print(bool(0))           # False, jo nulle nozīmē 'nekā nav'

# 4. Trīs datu tipu maiņas (pārveidošana)
print("--- Tipu maiņas piemēri ---")

# Pārvēršu tekstu par skaitli
skaitlis_no_teksta = int("10")
print(skaitlis_no_teksta)

# Pārvēršu skaitli par decimālskaitli (ar komatu)
ar_komatu = float(5)
print(ar_komatu)  # Izvadīs 5.0

# ROBEŽGADĪJUMS: mēģinu pārvērst kaut ko neiespējamu
# int("kūka") -> Šis izraisītu ValueError, jo vārdu nevar pārvērst cipros!
print("SVARĪGI: vārdus (kā 'kūka') nevar pārvērst par int, tas metīs kļūdu!")

print("--- Uzdevums pabeigts! ---")