woordenbestand = open('woorden.txt', 'rt')
woordenlijst = woordenbestand.read().splitlines()
woordenbestand.close()


# 1: totaal aantal woorden
def totaalaantal():
    aantalwoorden = 0
    for woord in woordenlijst:
            aantalwoorden +=1

    print('totaal aantal woorden =', aantalwoorden)

#2: het woord met de meeste letters
def meesteletters():
    langste_woord = ''
    lengte_1 = 0
    for woord in woordenlijst:
        lengte_2 = 0
        for letter in woord:
            lengte_2 += 1
        if lengte_2 > lengte_1:
            lengte_1 = lengte_2
            langste_woord = woord

    print('langste woord =', langste_woord)

#3: palindromen

def palindromen():
    palindromen_lijst = []
    for woord in woordenlijst:
            omgekeerd_woord = woord[::-1]
            if len(woord) > 1 and woord == omgekeerd_woord:
                palindromen_lijst.append(woord)
    print('lijst met palindromen:', palindromen_lijst)

    

#4: omgekeerd voorkomende woorden

def omgekeerd_voorkomend():
    result = set(woordenlijst)
    for woord in woordenlijst:
        omgekeerd_woord = woord[::-1]
        if len(woord) > 1 and omgekeerd_woord != woord and omgekeerd_woord in result:
                    print(woord, '-->', omgekeerd_woord)

    
#5: komt een ingevoerd woord voor

def ingevoerd_woord(): 
    invoer_woord = input('voer hier een woord in: ')
    woord_gevonden = 0
    for woord in woordenlijst:
        zoeken = woord.lower().find(invoer_woord.lower())
        if zoeken == 0:
            print("Je input:", invoer_woord, "is gevonden in:", woord)
            woord_gevonden +=1

    if woord_gevonden == 0:
        print('Je input is niet gevonden')


#6: woorden die je kunt maken van een ingevoerd woord

def anagram():
    invoer_woord = input('voer hier een woord in: ')

    geen_woorden = 0
    for woord in woordenlijst:
        if invoer_woord.lower() != woord.lower() and sorted(invoer_woord.lower()) == sorted(woord.lower()):
            print(woord)
            geen_woorden += 1

    if geen_woorden == 0:
        print('met deze input kun je geen anagram maken')

#7: woorden die rijmen op een ingevoerd woord
#oplossing voor woorden die eindigen op een klinker

def rijmwoorden_zoekklinker():
    invoer = input('voer een woord in: ').lower()
    klinkers = ['a', 'e', 'i', 'o', 'u']
    klinker_laatste_locatie = 0
    for letter in klinkers:
        klinker_locatie = invoer.rfind(letter)
        if klinker_locatie > klinker_laatste_locatie:
            klinker_laatste_locatie = klinker_locatie
    rijmwoorden(klinker_laatste_locatie, invoer)

def rijmwoorden(eersteklinker, invoer_woord):
    print(f'woorden die rijmen op {invoer_woord}')
    klank_letters = ['ou', 'ei', 'ai', 'ij', 'au', 'eu', 'oe', 'ui', 'ee']
    #controleren of er een klank van twee letters aan het einde van invoerwoord zit
    klanktest_invoerwoord_resultaat = False
    gevonden = ''
    for letters in klank_letters:
        klanktest_invoerwoord = klanktest(letters, invoer_woord[eersteklinker-1::])
        if klanktest_invoerwoord:
            klanktest_invoerwoord_resultaat = True
            gevonden = letters
    if klanktest_invoerwoord_resultaat == True:
        for woord in woordenlijst:
            if woord != invoer_woord:
                if invoer_woord[eersteklinker-1::] == woord[eersteklinker-1::]:
                    print(woord)
    if klanktest_invoerwoord_resultaat == False:
        for woord in woordenlijst:
            if woord != invoer_woord:
                dubbele_klanken_gevonden = False
                for letters2 in klank_letters:
                    klanktest_woord_uit_lijst = klanktest(letters2, woord[eersteklinker-1::])
                    if klanktest_woord_uit_lijst:
                        dubbele_klanken_gevonden = True
                if invoer_woord[eersteklinker::] == woord.lower()[eersteklinker::] and dubbele_klanken_gevonden == False:
                    print(woord)
 
def klanktest(letters, invoer):
    if letters in invoer:
        return letters
    else:
        return False

#8: Maak een raadspel, waarbij je alle letters van het woord in alfabetische volgorde plaatst en waar de gebruiker
# het oorspronkelijke woord moet raden

def raadspel():
    from random import randint
    lengte = len(woordenlijst) -1
    random_woord = woordenlijst[randint(0, lengte)]
    woord_sorted = sorted(random_woord)
    geraden = False

    while geraden == False:
        print("De letters van het woord in alfabetsiche volgorde: ",woord_sorted)
        geraden_woord = input("raad het woord: ")
        if geraden_woord.lower() == random_woord.lower():
            print("Dat klopt! Het woord was", random_woord)
            geraden = True
        else:
            print("Helaas, probeer het nog een keer")

#totaalaantal()
#meesteletters()
#palindromen()
#omgekeerd_voorkomend()
#ingevoerd_woord()
#anagram()
rijmwoorden_zoekklinker()
#raadspel()