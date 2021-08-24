from behave import *

#de functie die controleert of je het geld over mag maken
def allow_transfer_money(balance, amount, max_amount):
    if amount > 0 and amount <= max_amount and amount <= balance:
        return True
    else:
        return False

@given(u'I have 5000 euro in my bank account')
def step_impl(context):
    context.saldo = 5000


@given(u'my bank allows me to transfer 1000 euro max')
def step_impl(context):
    context.max_overboeken = 1000

@when(u'I transfer {hoeveelheid_overboeken} euro to my friends bank account')
def step_impl(context, hoeveelheid_overboeken):
    #zet de functie in die controleert of je overboeking mogelijk is
    context.overboeking = allow_transfer_money(context.saldo, int(hoeveelheid_overboeken), context.max_overboeken)

@then(u'the money has {wel_of_niet} been transferred')
def step_impl(context, wel_of_niet):
    #controleer of de overboeking wel of niet mogelijk was
    if wel_of_niet == 'not':
        assert context.overboeking == False
    else:
        assert context.overboeking
 
