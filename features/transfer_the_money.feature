
Feature: Transfer from my bank account

Background:
    Given I have 5000 euro in my bank account
    And my bank allows me to transfer 1000 euro max

Scenario Outline: Transferring an amount of money
    When I transfer <amount> euro to my friends bank account
    Then the money has <wel_niet> been transferred
    Examples:
        	| amount | wel_niet     |
            | -1     | not          |
            | 0      | not          |
            | 1      | successfully |
            | 999    | successfully |
            | 1000   | successfully |
            | 1001   | not          |
            | 4999   | not          |
            | 5000   | not          |
            | 5001   | not          |