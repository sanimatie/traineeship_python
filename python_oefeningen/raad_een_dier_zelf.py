#importeer de json file met de dictionary
import json

json_file = open('Dieren_JSON.json', 'rt')
dieren = json.loads(json_file.read())
json_file.close()

def keuze_menu():
    print('Wat wil je doen?\n 1. Het spel spelen\n 2. Een vraag aanpassen\n 3. Alle dieren in de database zien \n 4. Stoppen')
    nummer = input()
    if nummer == '1':
        start_spel()
    elif nummer == '2':
        vragen_updaten_totaal()
    elif nummer == '3':
        print('\033[4;37;40mAlle dieren in de database:\033[0;0m')
        verzamel_alle_dieren(dieren)
        print('\n')
        keuze_menu()
    elif nummer == '4':
        print('Tot de volgende keer!')
    else:
        print('Voer een geldig nummer in')
        keuze_menu()


def start_spel():
    print('\033[4;37;40mNeem een dier in gedachten..\033[0;0m\n')
    spel_starten = ja_of_nee('Ben je er klaar voor?')
    if spel_starten == 'ja':
        #start de formule met de recursie, met dictionary 'dieren' als parameter
        vragen(dieren)

def vragen(tak):
    #de functie formatting zorgt dat elke vraag een hoofdletter en vraagteken heeft
    vraag = formatting(tak)
    antwoord_vraag = ja_of_nee(vraag)

    # controleren of een tak eindigt met een dier of nog een vraag
    uitkomst = isinstance(tak[antwoord_vraag], dict)
    #volgende vraag stellen
    if uitkomst:
        vragen(tak[antwoord_vraag])
    #uitkomst dier geven
    else:
        antwoord_einde = ja_of_nee('Dacht je aan een '+ tak[antwoord_vraag]+'?')
        if antwoord_einde == 'ja':
            print('\033[0;32;40mHoera! Ik had het goed geraden!\033[0;0m')
            opnieuw_spelen()
        else:
            #maak een nieuw dier
            nieuw_dier(tak, antwoord_vraag)
            opnieuw_spelen()


#vragen format (vraagtekens, hoofdletters)
def formatting(tak):
    vraag = tak['vraag'].capitalize()
    if vraag.endswith('?'):
        return vraag
    else:
        vraag += '?'
        return vraag

#ja of nee invullen
def ja_of_nee(vraag):
    antwoord = input(vraag + ' ')
    if antwoord.startswith('j'):
        antwoord = 'ja'
        return antwoord
    else:
        antwoord = 'nee'
        return antwoord

def nieuw_dier(tak, richting):
    oud_dier = tak[richting]
    antwoord_nieuw_dier = input('Aan welk dier dacht je dan? ').lower()
    #'een ' weghalen als het voor de naam van het dier is getypt
    if antwoord_nieuw_dier.startswith('een '):
        antwoord_nieuw_dier = antwoord_nieuw_dier.replace('een ', '')
    #een nieuwe vraag laten invullen en evt vraagtekens en punten weghalen
    nieuwe_vraag(tak, richting, antwoord_nieuw_dier, oud_dier, f'Welke vraag had ik moeten stellen om {antwoord_nieuw_dier} te kunnen raden in plaats van {oud_dier}? ')
 
    
def nieuwe_vraag(tak, richting, nieuw_dier, oud_dier, input_tekst):
    nieuwe_vraag_input_tekst = input(input_tekst).lower().replace('?', '').replace('.', '')
    print('\n\033[4;37;40mDe nieuwe vraag en de bijbehorende antwoorden: \033[0;0m\n')
    print(f'\033[3;37;40m{nieuwe_vraag_input_tekst.capitalize()}?')
    print('\033[1;37;40mja:\033[0;0m', nieuw_dier, ' \033[1;37;40mnee:\033[0;0m', oud_dier, '\n')
    antwoord = ja_of_nee('Klopt dit?')
    if antwoord == 'ja':
        tak[richting] = {'vraag': nieuwe_vraag_input_tekst, 'ja': nieuw_dier, 'nee': oud_dier}
        print('\033[0;32;40mHet nieuwe dier en de vraag zijn toegevoegd!\033[0;0m')
    else:
        nieuwe_vraag(tak, richting, nieuw_dier, oud_dier, 'Stel een andere vraag: ')

def vraag_en_dier_toevoegen(tak, richting, nieuwe_vraag_input_tekst, oud_dier):
    tak[richting] = {'vraag': nieuwe_vraag_input_tekst, 'ja': nieuw_dier, 'nee': oud_dier}
    print('\033[0;32;40mHet nieuwe dier en de vraag zijn toegevoegd!\033[0;0m')

def opnieuw_spelen():
    opnieuw = ja_of_nee('Wil je nog een keer spelen?')
    if opnieuw == 'ja':
        vragen(dieren)
    else:
       print('Jammer! Tot de volgende keer!')
       keuze_menu()



#vragen aanpassen

vragen_array = []
vraag_nummer = 1

#alle vragen verzamelen in een array
def vragen_lijst(tak):
    if isinstance(tak, dict):
        vraag = formatting(tak)
        vragen_array.append(vraag)
        for richting in tak:
            vragen_lijst(tak[richting])

#alle vragen printen met een bijbehorend nummer
def vragen_nummeren(vragen_array, vraag_nummer):
    for vraag in vragen_array:
        print('\033[1;36;40m',vraag_nummer, ': \033[0;0m', vraag)
        vraag_nummer +=1

def vraag_aanpassen(welk_nummer):
    try:
        vraag_nummer = int(input(welk_nummer))
        if vraag_nummer >= 1 and vraag_nummer <= len(vragen_array):
            nieuwe_vraag = input('Vul de nieuwe vraag in: ')
            vragen_array[vraag_nummer-1] = nieuwe_vraag
            print('\033[0;32;40mDe vraag is aangepast!\033[0;0m')
            keuze_menu()
                
        else: 
            print('\033[0;31;40mGeen geldige invoer.\033[0;0m')
            vraag_aanpassen('Voer het nummer in dat voor de vraag staat die je aan wil passen: ')
    except:
        print('\033[0;31;40mGeen geldige invoer.\033[0;0m')
        vraag_aanpassen('Voer het nummer in dat voor de vraag staat die je aan wil passen: ')


def vragen_updaten(tak, vragen_array):
    if isinstance(tak, dict):
        tak['vraag'] = vragen_array[0].lower().replace('?', '').replace('.', '')
        del vragen_array[0]
        for richting in tak:
            vragen_updaten(tak[richting], vragen_array)


def vragen_updaten_totaal():
    vragen_lijst(dieren)
    vragen_nummeren(vragen_array, vraag_nummer)
    vraag_aanpassen('Welke vraag wil je aanpassen?')
    vragen_updaten(dieren, vragen_array)


#lijst met alle dieren maken

def verzamel_alle_dieren(tak):
    if isinstance(tak['ja'], dict):
        verzamel_alle_dieren(tak['ja'])
    else: print(tak['ja'])

    if isinstance(tak['nee'], dict):
        verzamel_alle_dieren(tak['nee'])
    else:
        print(tak['nee'])

#start_spel()
#vragen_updaten_totaal()
#verzamel_alle_dieren(dieren)
keuze_menu()


#nieuwe dictionary opslaan

json_einde = open('Dieren_JSON.json','wt')
json_einde.write(json.dumps(dieren))
json_einde.close()

