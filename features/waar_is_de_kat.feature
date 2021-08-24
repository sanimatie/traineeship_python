
Feature: Waar is de kat geweest

Scenario: Winning the game
    Given the cat is hiding in box 3
    And the amount of attempts is 0
    When I look in box 3
    Then the game will tell me I have won
    And the amount of attempts will be 1

Scenario Outline: Picking a box without the cat
    Given the cat is hiding in box <box_number>
    And the amount of attempts is 0
    When I look in box 3
    Then the cat will move to box <box_left> or <box_right>
    And the amount of attempts will be 1
    And the game will continue

    Examples:
    | box_number | box_left | box_right |
    | 1          | False    | 2         |
    | 4          | 3        | 5         |
    | 5          | 4        | False     | 

Scenario Outline: Wrong input
    Given the cat is hiding in box 3
    And the amount of attempts is 0
    When I look in box <invalid_input>
    Then the game will tell me to put in a valid number
    And the amount of attempts will be 0
    And the game will continue
    And the cat will still be hiding in box 3

    Examples:
    | invalid_input |
    | 6             |
    | string        |
    | -1            |
    | 0             |
    | !             |