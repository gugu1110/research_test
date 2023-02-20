Scenario: Test Windows Calculator
    Given the Windows Calculator is open
    When I press the "1" button
    And I press the "+" button
    And I press the "2" button
    And I press the "=" button
    Then the result should be "3"
