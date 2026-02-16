# --- MANAS KONSTANTES ---
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172

print("Sveiki! Pārversim mērvienības")

# 1. Lietotājs izvēlas kategoriju
print("Ko vajag konvertēt? 1) km/mi  2) kg/lb  3) L/gal")
izvēle = input("Ievadi ciparu: ")

# 2. Lietotājs izvēlas virzienu
print("Virziens: 1) No kreisās uz labo  2) No labās uz kreiso")
virziens = input("Ievadi ciparu: ")

# 3. Ievada vērtību (pārvēršam par float)
vertība = float(input("Cik daudz? "))

# --- APRĒĶINI ---

# Kilometri un jūdzes
if izvēle == "1":
    if virziens == "1":
        rezultāts = vertība * KM_TO_MI
        print(f"{vertība:.2f} km ir {rezultāts:.2f} jūdzes")
    else:
        rezultāts = vertība / KM_TO_MI
        print(f"{vertība:.2f} jūdzes ir {rezultāts:.2f} km")

# Kilogrami un mārciņas
elif izvēle == "2":
    if virziens == "1":
        rezultāts = vertība * KG_TO_LB
        print(f"{vertība:.2f} kg ir {rezultāts:.2f} lb")
    else:
        rezultāts = vertība / KG_TO_LB
        print(f"{vertība:.2f} lb ir {rezultāts:.2f} kg")

# Litri un galoni
elif izvēle == "3":
    if virziens == "1":
        rezultāts = vertība * L_TO_GAL
        print(f"{vertība:.2f} L ir {rezultāts:.2f} gal")
    else:
        rezultāts = vertība / L_TO_GAL
        print(f"{vertība:.2f} gal ir {rezultāts:.2f} L")

else:
    print("Oi, kaut kas nesanāca ar izvēli!")

print("Paldies un jauku Jums dienu!")
