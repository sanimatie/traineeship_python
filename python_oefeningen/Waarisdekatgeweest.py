from random import randint
from random import choice

aantal_dozen = 5
aantal_pogingen = 0
kat_gevonden = False
doos_met_kat = randint(1, aantal_dozen)
#print("startpositie: ", doos_met_kat)

while kat_gevonden == False:
    #print("kat zit in doos: ", doos_met_kat)
    try:
        input_tekst = input("Kies een doos om te openen, of type 'stoppen' om te stoppen: ")
        if input_tekst == 'stoppen':
            kat_gevonden = True
        else:
            input_nummer = int(input_tekst)
            if input_nummer > 0 and input_nummer <= 5:
                if doos_met_kat == input_nummer:
                    kat_gevonden = True
                    aantal_pogingen += 1
                    print("Kat gevonden!\U0001f63a")
                    print("Aantal pogingen: ", aantal_pogingen)
                else: 
                    aantal_pogingen += 1
                    print(f"Kat niet gevonden in doos {input_nummer}, probeer het nog een keer.")
                    print(f"Aantal pogingen: {aantal_pogingen}")
                    if doos_met_kat == aantal_dozen:
                        doos_met_kat -= 1
                    #    print("kat naar links: ")
                    elif doos_met_kat == 1:
                        doos_met_kat += 1
                    #    print("kat naar rechts: ")
                    else:
                        doos_met_kat += choice([-1, 1])
                    #    print("kat zit in: ", doos_met_kat)
            else:
                print("dit is geen bestaande doos, kies een nummer tussen 1 en ", aantal_dozen)
    except:
        print("vul een geldig nummer in")
