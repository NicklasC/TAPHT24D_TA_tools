Feature: test sum and number of books
  Test combinations of books and numbers of books and verify they are grouped correctly.
  Sum should also be correct.

  Background:
    Given user is on start page with an empty cart

  Scenario Outline: Book combinations
    Given that I order <book_1>
    And that I order <book_2>
    And that I order <book_3>
    Then <expected_listed_number_of_books> book titles should be listed
    And the total order sum should be <total_order_sum>

    Examples:

  # Assumed prices for each book
  #  - Book A: $10
  #  - Book B: $15
  #  - Book C: $20

  | book_1 | book_2 | book_3 | expected_listed_number_of_books | total_order_sum |
  # All unique books
  | A      | B      | C      | 3                               | 45              |
  # A is added twice
  | A      | A      | B      | 2                               | 35              |
  # Only B added multiple times
  | B      | B      | B      | 1                               | 45              |
  # C is added twice, A once
  | C      | A      | C      | 2                               | 50              |
  # A is added three times
  | A      | A      | A      | 1                               | 30              |
  # Unique books in different order
  | B      | C      | A      | 3                               | 45              |
  # Only C added multiple times
  | C      | C      | C      | 1                               | 60              |