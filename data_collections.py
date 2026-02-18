# --- A daļa: Saraksti ---
# 1. Izveidot sarakstu ar 5+ skaitļiem
skaitļi = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pievienojam 10, uzdevums par .append()
skaitļi.append(10) 

# TAGAD izdzēšam to pēdējo elementu (10) ar .pop()
skaitļi.pop()

# 2. Aprēķinam summu un vidējo (bez sum() un len())
summa = 0
skaits = 0
for s in skaitļi:
    summa += s
    skaits += 1

vidējais = summa / skaits
print(f"Summa: {summa}, Vidējais: {vidējais}")

# 3. Filtrē tikai pāra skaitļus
pāra_skaitļi = []
for s in skaitļi:
    if s % 2 == 0:
        pāra_skaitļi.append(s)
print(f"Pāra skaitļi: {pāra_skaitļi}")

# 4. Demonstrē šķēlumu (slice)
pirmie_3 = skaitļi[:3]
pēdējie_2 = skaitļi[-2:]
katrs_otrais = skaitļi[::2]
print(f"Pirmie 3: {pirmie_3}, Pēdējie 2: {pēdējie_2}")


# --- B daļa: Vārdnīcas ---
print("\n--- Vārdnīcas ---")

# 1. Izveidot vārdnīcu
studenti = {"Anna": 85, "Jānis": 72, "Līga": 95}

# 2. Pievienos jauno un mainīs jau esošu
studenti["Viktorija"] = 60
studenti["Jānis"] = 75  # Mainām atzīmi Jānim

# 3. Iterē un izvada katru
for vārds, atzīme in studenti.items():
    print(f"{vārds}: {atzīme}")

# 4. Atrod studentu ar augstāko atzīmi
labākais_vārds = ""
max_atzīme = 0

for vārds, atzīme in studenti.items():
    if atzīme > max_atzīme:
        max_atzīme = atzīme
        labākais_vārds = vārds

print(f"Labākais students: {labākais_vārds} ({max_atzīme})")


# --- C daļa: Kombinācija ---
print("\n--- Studenti ar atzīmi >= 80 ---")

# 1. Saraksts ar vārdnīcām
studentu_saraksts = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 72},
    {"name": "Līga", "grade": 95},
    {"name": "Viktorija", "grade": 60}
]

# 2. Filtrēšana: atlasām tikai tos, kam atzīme ir 80 vai vairāk
labākie_studenti = [] 
for students in studentu_saraksts:
    if students["grade"] >= 80:
        labākie_studenti.append(students)

# 3. Sakārtošana: lai saraksta augšgalā būtu lielākā atzīme
labākie_studenti.sort(key=lambda x: x["grade"], reverse=True)

print("Filtrēšana un kārtošana pabeigta!\n")

# 4. Skaista izvade: izmantojam enumerate(), lai pieliktu punktus (1., 2. utt.)
for i, students in enumerate(labākie_studenti, start=1):
    vārds = students["name"]
    atzīme = students["grade"]
    
    # f-string saliek visu vienā skaistā rindiņā
    print(f"{i}. {vārds} — {atzīme}")