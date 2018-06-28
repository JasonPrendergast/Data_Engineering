
Feature: test cases HandleinputDB_handle_all_tables
  #background will run before every scenario
  Background: Create HandleinputDB_handle_all_tables context variables
    Given I create new HandleinputDB_handle_all_tables context variables

  Scenario Outline: "<table_name1>"  and "<table_name1>" and "<file>" and "<inc_response>"and "<equals>"
    Given I have names table <table_name1> <table_name1>
    And I have file name <file>
    And I have response <inc_response>
    When I call handle_all_tables
    Then I should see handle_all_tables <equals>

  Examples:
    | table_name1 | table_name1| file |  inc_response | equals |
    | police      | response   | test |  0            | True   |
    | police      | response   | test |  1            | True   |
    | ''          | ''         | test |  1            | False  |

