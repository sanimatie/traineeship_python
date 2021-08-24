
Feature: Exercise with examples and a Data Table

  In deze feature zitten twee scenario's die data aan de steps doorgeven.
  We maken gebruik van een Scenario Outline en een Data Table.

  In de step implementatie maken we een bestand waarin de gegevens uit de
  Examples en Data Table worden weggeschreven.

Scenario: Create a file
    Given There is an empty text file available to us
    When I write the following table in it
      | course          | participants |
      | Behave          | 213          |
      | Cucumber        | 0            |
      | Robot Framework | 42           |
    And I open this file and check the number of lines
    Then This file has 3 lines in it

 Scenario Outline: some records
    Given The text file has been opened
    Then I write the values <first>, <second> and <third> 
    And I close the file

    Examples:
      | first | second | third     |
      | one   | monkey | monday    |
      | two   | cow    | tuesday   |
      | three | moose  | wednesday |
      | four  | dodo   | thursday  |