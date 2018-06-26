
Feature: test cases HandleinputDB_database_to_df
  #background will run before every scenario
  Background: Create HandleinputDB_database_to_df context variables
    Given I create new HandleinputDB_database_to_df context variables

  Scenario Outline: "<table>"  and "<equals>"
    Given I have table <table>
    When I call database_to_df
    Then I should see database_to_df <equals>

  Examples:
    |  table                          | equals |
    |  police                         | True   |
    |  response                       | True   |
    |  Not_a_table                    | False  |



