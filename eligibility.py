print("--- Atbilstības pārbaudītājs ---")

# 1. Datu ievāde
ievāde = input("Lūdzu ievādīt klienta vecumu: ")

# Pārbaudām, vai ievadīts skaitlis un vai tas nav negatīvs
if not ievāde.isnumeric():
    print("❌ Kļūda: Lūdzu, ievadīt vecumu ciparos!")
else:
    vecums = int(ievāde)
    
    if vecums < 0:
        print("❌ Kļūda: Vecums nevar būt negatīvs!")
    else:
        # Ievedam pārējo info (jā/nē -> True/False)
        ir_apliecība = input("Vai ir autovadītāja apliecība? (jā/nē): ").lower() == 'j'
        ir_students = input("Vai ir students? (jā/nē): ").lower() == 'j'
        ir_veterāns = input("Vai ir veterāns? (jā/nē): ").lower() == 'j'

        # 2. Loģikas pārbaude
        var_balsot = vecums >= 18
        var_īrēt_auto = vecums >= 21 and ir_apliecība
        senjoru_atlaide = vecums >= 65 or ir_veterāns
        studentu_atlaide = 16 <= vecums <= 26 and ir_students

        # 3. Rezultātu izvade ar f-string
        print("\n--- REZULTĀTI ---")
        
        # Izmantojam vienkāršu "Jā" vai "Nē" loģiku izvadei
        print(f"Balsošana:       {'Jā ✅' if var_balsot else 'Nē ❌'}")
        
        # Papildu paskaidrojums auto īrei, ja nav apliecības
        auto_teksts = "Jā ✅" if var_īrēt_auto else "Nē ❌"
        if vecums >= 21 and not ir_apliecība:
            auto_teksts += " (nav apliecības)"
        print(f"Auto īre:        {auto_teksts}")
        
        print(f"Senjoru atlaide: {'Jā ✅' if senjoru_atlaide else 'Nē ❌'}")
        print(f"Studentu atlaide:{'Jā ✅' if studentu_atlaide else 'Nē ❌'}")
