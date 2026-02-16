import random  # Šis ļauj datoram izdomāt nejaušu skaitli

print("Apsveicu, Jūs esat skaitļu minēšanas spēlē!")

while True:  # Ārējais cikls, lai varētu spēlēt vēlreiz
    ierīces_skaitlis = random.randint(1, 100)
    mēģinājumu_skaits = 0
    max_mēģinājumi = 10
    
    print("\n Es iedomājos skaitli no 1 līdz 100. Tev ir 10 mēģinājumi!")

    while mēģinājumu_skaits < max_mēģinājumi:
        ievade = input(f"Mēģinājums {mēģinājumu_skaits + 1}: Tavs minējums? ")

        # 1. Pārbaudām, vai ievadītais tiešām ir skaitlis
        if not ievade.isnumeric():
            print("❌ Lūdzu, ievadi ciparu!")
            continue  # Atgriežas uz cikla sākumu, neatņemot mēģinājumu

        minējums = int(ievade)
        mēģinājumu_skaits += 1

        # 2. Salīdzinām minējumu ar datora skaitli
        if minējums < ierīces_skaitlis:
            print("📈 Par mazu! Pamēģini lielāku.")
        elif minējums > ierīces_skaitlis:
            print("📉 Par lielu! Pamēģini mazāku.")
        else:
            print(f"🥳 APSVEICU! Tu uzminēji {ierīces_skaitlis} ar {mēģinājumu_skaits}. mēģinājumu!")
            break  # Iziet no minēšanas cikla
            
        # 3. Ja mēģinājumi beigušies
        if mēģinājumu_skaits == max_mēģinājumi:
            print(f"Diemžel, mēģinājumi beidzās. Mans skaitlis bija {ierīces_skaitlis}.")

    # 4. Pajautājam, vai spēlēt vēlreiz
    velreiz = input("\nVai vēlies spēlēt vēlreiz? (jā/nē): ").lower()
    if velreiz != 'j':
        print("👋 Paldies par spēli! Uz redzēšanos!")
        break
