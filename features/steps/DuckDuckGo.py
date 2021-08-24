from behave import *
from splinter.browser import Browser
import logging
from hamcrest import assert_that, equal_to

@given(u'the Chrome webbrowser has been opened')
def step_impl(context):
    context.browser = Browser('chrome')  

@when(u'I visit https://duckduckgo.com')
def step_impl(context):
    context.browser.visit("https://duckduckgo.com")

@when(u'I type "potatoes" in the search bar')
def step_impl(context):
    context.browser.fill('q', 'potatoes') 


@when(u'I click the search button')
def step_impl(context):
    button = context.browser.find_by_id('search_button_homepage')
    button.click() 


@then(u'the webpage will show me search results for "potatoes"')
def step_impl(context):
    logging.info('test2')
    gevonden = context.browser.find_link_by_partial_text('potatoes')
    context.browser.find_by_value('potatoes')
    #assert 'potatoes' in context.browser.html
    #assert_that(context.browser.html, has_string('hee'))
    #assert 'potatoes' in browser.title
    if gevonden:
        logging.info('De test is geslaagd')
    else:
        logging.info('potatoes wordt niet gevonden')
    assert context.browser.find_link_by_partial_text('potatoes')
    #assert context.browser.find_link_by_href('https://en.wikipedia.org/wiki/Potato')

