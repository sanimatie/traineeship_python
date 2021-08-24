from splinter.browser import Browser                   # importeer de Browser klasse
from time import sleep

browser = Browser('chrome')                            # instantieer een browser object
browser.visit("https://duckduckgo.com")                # laat de browser naar een URL navigeren
browser.fill('q', 'aardappel')                         # vul een zoektekst in, 'q' is hier de naam van de zoekbalk
button = browser.find_by_id('search_button_homepage')  # Zoek de Zoek knop
button.click()                                         # Druk op de knop
sleep(30)
browser.quit()                                         # Sluit de browser
