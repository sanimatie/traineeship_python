from behave import *

def create_text_file(filename):
    f = open(filename, "wt")
    f.close()

def check_lines(filename):
    aantal_regels = 0
    f = open(filename, "rt")
    for regel in f:
        aantal_regels += 1
    f.close()
    return aantal_regels

def add_line_to_file(filename, this_line):
    f = open(filename, "at")
    f.write(this_line + "\n")
    f.close()

@given(u'There is an empty text file available to us')
def step_impl(context):
    create_text_file('nieuw_bestand.txt')

@when(u'I write the following table in it')
def step_impl(context):
    for row in context.table:
        course = row["course"]
        participant = row["participants"]
        nieuwe_regel = course + '\t' + participant
        add_line_to_file('nieuw_bestand.txt', nieuwe_regel)

@when(u'I open this file and check the number of lines')
def step_impl(context):
    context.aantal_regels = check_lines('nieuw_bestand.txt')

@then(u'This file has 3 lines in it')
def step_impl(context):
    assert context.aantal_regels == 3

@given(u'The text file has been opened')
def step_impl(context):
    context.bestand = open('nieuw_bestand.txt', 'at')


@then(u'I write the values {one}, {two} and {three}')
def step_impl(context, one, two, three):
    assert context.bestand.write(one + '\t' + two + '\t' + three + '\n')


@then(u'I close the file')
def step_impl(context):
    context.bestand.close()
    assert context.bestand.closed