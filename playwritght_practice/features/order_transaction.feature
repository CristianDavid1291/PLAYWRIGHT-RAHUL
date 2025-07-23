Feature: Order Transaction
  As a customer
  I want to place an order and verify it
  So that I can confirm my purchase was successful

  Scenario Outline: Place order and verify transaction
    Given place the item order with <username> and <password>
    And the user is on landing page
    When the user logs in with <username> and <password>
    And select the orderId
    Then order success message should be shown in details page

    Examples:
      | username                    | password        |
      | cristiandavid1291@gmail.com | Manizales2025++ |
