Feature: add and remove items to/from cart

  Scenario: Add item to cart
    Given User is on start page with an empty cart
    When User adds first item to cart
    Then Cart should contain one item


  Scenario: Remove item from cart
    Given User is on start page with one item in the cart
    When User removes first item from cart
    Then Cart should be empty
