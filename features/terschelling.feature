@wip
Feature: Terschelling regression tests

Background:
    Given I have opened the website https://www.vvvterschelling.nl/
    And I have accepted the cookies

Scenario Outline: Een categorie aanklikken
    When I click on the category <category_name>
    Then <checkpoint> will appear on the page <checkpoint_type>
     And I will be on the page https://www.vvvterschelling.nl/<url>

    Examples:
        | category_name                       | checkpoint_type      | checkpoint           | url                              |
        | Bunkers op Terschelling             | in the text          | Tweede Wereldoorlog  | bunkers-op-terschelling          |
        | Terschelling Challenge              | repeatedly in a link | lees verder >        | terschelling-challenge           |
        | Uitzichtpunten                      | repeatedly in a link | Uitzichtpunt         | uitzichtpunten                   |
        | De Boot naar Terschelling           | in an id             | ferry-route          | de-boot-naar-terschelling        |
        | Bezienswaardigheden op Terschelling | in an id             | search-filter-toggle | bezienswaardigheden-terschelling |
        | JutXL                               | in the text          | JutXL                | jutxl                            |

Scenario: zoeken naar campings
    When I click on the search button
     And I type in camping
     And I click on 'Zoeken'
    Then camping will appear on the page repeatedly in a link

Scenario: bedrijven filteren
    When I click on the category Bedrijven
     And I click on the category Kerken
     And I click on the category Midsland Noord
    Then Protestantse Gemeente, ET-10 will appear on the page in the text

Scenario: Arrangementen vandaag
    When I click on the category Arrangementen
     And I click on "Vandaag"
    Then the page will show me arrangement results for today
