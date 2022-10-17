Feature: Automation Practice browsing
    As a SDET
    I want to browse automationpractice website
    So that I can buy a product


Background:
    Given the automationpractice website is displayed

Scenario: Buy TShirt
    When the user clicks on TShirts
    And adds to the cart the "Faded Short Sleeve T-shirts"
    Then the user is redirected to checkout
    #     And the user can complete the purchase
