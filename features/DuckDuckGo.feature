
Feature: DuckDuckGo

Scenario: Search in DuckDuckGo
    Given the Chrome webbrowser has been opened
    When I visit https://duckduckgo.com
     And I type "potatoes" in the search bar
     And I click the search button
    Then the webpage will show me search results for "potatoes"