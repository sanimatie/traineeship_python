from behave import *
from splinter.browser import Browser
import time
from hamcrest import assert_that, equal_to, greater_than
from datetime import date

def test(plaats):
    browser = Browser('chrome')
    if plaats == 'terschelling':
        browser.visit('https://www.vvvterschelling.nl/')
    elif plaats == 'texel':
        browser.visit('https://www.texel.net/nl/')
    button = browser.find_by_text('Akkoord')
    time.sleep(5)
    button.click()
    time.sleep(5)
#test('texel')

#background
@given(u'I have opened the website https://www.vvvterschelling.nl/')        
def step_impl(context):
    context.browser = Browser('chrome')
    context.browser.visit('https://www.vvvterschelling.nl/')

@given(u'I have accepted the cookies')
def step_impl(context):
    button = context.browser.find_by_text('✓ Ja, ik ga akkoord')
    button.click()

#klik op een href link adhv gevonden tekst
@when(u'I click on the category {category_name}')
def step_impl(context, category_name):
    button = context.browser.links.find_by_partial_text(category_name)
    button.click()

#controleren of iets op een pagina staat
@then(u'{checkpoint} will appear on the page {checkpoint_type}')
def step_impl(context, checkpoint_type, checkpoint):
    if checkpoint_type == 'in the text':
        assert context.browser.is_text_present(checkpoint)
    elif checkpoint_type == 'repeatedly in a link':
        #controleer of een bepaalde tekst een paar keer voorkomt in een lijst met links
        checkpoint_lijst = context.browser.links.find_by_partial_text(checkpoint)
        aantal_keer = len(checkpoint_lijst)
        assert_that(aantal_keer, greater_than(3))
    elif checkpoint_type == 'in an id':
        context.browser.is_element_present_by_id(checkpoint)
    #geef een error als een step niet voorkomt in de if/else statements
    else: 
        assert False

#controleer een url
@then(u'I will be on the page https://www.vvvterschelling.nl/{url}')
def step_impl(context, url):
    assert_that(context.browser.url, equal_to(f'https://www.vvvterschelling.nl/{url}'))
    context.browser.quit()

#gebruikmaken van de zoekfunctie
@when(u'I click on the search button')
def step_impl(context):
    button = context.browser.find_by_css('.search-toggle')
    button.click()

@when(u'I type in camping')
def step_impl(context):
    context.browser.fill('query', 'camping')

@when(u'I click on \'Zoeken\'')
def step_impl(context):
    button = context.browser.find_by_id('edit-submit')
    button.click()

#arrangementen vandaag

@when(u'I click on "Vandaag"')
def step_impl(context):
    button = context.browser.find_by_id('edit-today')
    button.click()


@then(u'the page will show me arrangement results for today')   
def step_impl(context):
    #vind de datum van vandaag en zet hem om naar hetzelfde format als de data op de site
    vandaag = date.today()
    vandaag = vandaag.strftime("%d-%m-%Y")
    #vind de data die in de velden 'van' en 'tot' zijn ingevuld
    datum_van = context.browser.find_by_id('edit-from-datepicker-popup-0').value
    datum_tot = context.browser.find_by_id('edit-until-datepicker-popup-0').value
    #vergelijk de data van vandaag met de gevonden data
    assert_that(vandaag, equal_to(datum_van))
    assert_that(vandaag, equal_to(datum_tot))

