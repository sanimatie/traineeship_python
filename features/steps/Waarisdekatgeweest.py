from random import randint
from random import choice

aantal_dozen = 5
doos_met_kat = 3
#input_tekst = 3
spel_gewonnen = False
#gekozen_doos = 4

def waar_is_de_kat_geweest(doos_met_kat, spel_gewonnen):
    aantal_pogingen = 0
    while spel_gewonnen == False:
        gekozen_doos = input("Kies een doos om te openen, of type 'stoppen' om te stoppen: ")
        doos_met_kat, aantal_pogingen, spel_gewonnen, ongeldig_nummer = waar_is_de_kat_geweest_ronde(doos_met_kat, aantal_pogingen, spel_gewonnen, gekozen_doos)

def waar_is_de_kat_geweest_ronde(doos_met_kat, aantal_pogingen, spel_gewonnen, gekozen_doos):
        ongeldig_nummer = 0
        try:
            if gekozen_doos == 'stoppen':
                spel_gewonnen = True
            else:
                input_nummer = int(gekozen_doos)
                if input_nummer > 0 and input_nummer <= 5:
                    aantal_pogingen += 1
                    if doos_met_kat == input_nummer:
                        spel_gewonnen = gewonnen(aantal_pogingen)
                    else: 
                        doos_met_kat = verplaats_kat(aantal_pogingen, doos_met_kat, input_nummer)
                else:
                    print("dit is geen bestaande doos, kies een nummer tussen 1 en ", aantal_dozen)
                    ongeldig_nummer = 1
        except:
            print("vul een geldig nummer in")
            ongeldig_nummer = 1
        return doos_met_kat, aantal_pogingen, spel_gewonnen, ongeldig_nummer

def verplaats_kat(aantal_pogingen, doos_met_kat, input_nummer):
    print(f"Kat niet gevonden in doos {input_nummer}, probeer het nog een keer.")
    print(f"Aantal pogingen: {aantal_pogingen}")
    if doos_met_kat == aantal_dozen:
        doos_met_kat -= 1
    elif doos_met_kat == 1:
        doos_met_kat += 1
    else:
        doos_met_kat += choice([-1, 1])
    return doos_met_kat

def gewonnen(aantal_pogingen):
        print("Kat gevonden!\U0001f63a")
        print("Aantal pogingen: ", aantal_pogingen)
        return True

#waar_is_de_kat_geweest(doos_met_kat, spel_gewonnen)