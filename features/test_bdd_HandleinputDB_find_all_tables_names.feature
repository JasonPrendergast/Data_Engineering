
Feature: test cases HandleinputDB_find_all_tables_names
  #background will run before every scenario
  Background: Create HandleinputDB_find_all_tables_names context variables
    Given I create new HandleinputDB_find_all_tables_names context variables

  Scenario Outline: no params and <equals>
    When I call find_all_tables_names
    Then I should see find_all_tables_names <equals>

  Examples:
    | equals |
    | True   |



