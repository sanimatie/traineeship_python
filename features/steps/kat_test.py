from Waarisdekatgeweest import *
from behave import *

spel_gewonnen = False
#waar_is_de_kat_geweest(doos_met_kat, aantal_pogingen, spel_gewonnen, gekozen_doos)

@given(u'the cat is hiding in box {box_number}')
def step_impl(context, box_number):
    context.doos_met_kat = int(box_number)

@given(u'the amount of attempts is 0')
def step_impl(context):
    context.aantal_pogingen = 0    

@when(u'I look in box {input}')
def step_impl(context, input):
    uitkomst = waar_is_de_kat_geweest_ronde(context.doos_met_kat, context.aantal_pogingen, spel_gewonnen, input)
    context.nieuwe_doos = uitkomst[0]
    context.nieuw_aantal_pogingen = uitkomst[1]
    context.spel_gewonnen = uitkomst[2]
    context.ongeldig_nummer = uitkomst[3]

@then(u'the cat will still be hiding in box 3')
def step_impl(context):
    assert context.nieuwe_doos == 3

#kat verplaatst
@then(u'the cat will move to box {box_left} or {box_right}')
def step_impl(context, box_left, box_right):
    if box_left == 'False':
        assert context.nieuwe_doos == int(box_right)
    elif box_right == 'False':
        assert context.nieuwe_doos == int(box_left)
    elif context.nieuwe_doos == int(box_left) or context.nieuwe_doos == int(box_right):
        assert True
    else:
        assert False

#gewonnen
# @then(u'the game will {uitkomst}')
# def step_impl(context, uitkomst):
#      if uitkomst == 'tell me I have won':
#          assert context.spel_gewonnen == True
#          assert context.ongeldig_nummer == 0
#      elif uitkomst == 'continue':
#          assert context.spel_gewonnen == False 
#      elif uitkomst == 'tell me to put in a valid number':
#          assert context.ongeldig_nummer == 1


@then(u'the amount of attempts will be {amount}')
def step_impl(context, amount):
        assert context.nieuw_aantal_pogingen == int(amount)
