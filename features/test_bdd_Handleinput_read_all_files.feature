
Feature: test cases Handleinput_read_all_files
  #background will run before every scenario
  Background: Create Handleinput_read_all_files context variables
    Given I create new Handleinput_read_all_files context variables
# datapath, inc_db, inc_response, dbobj
  Scenario Outline: "<inc_db>" and "<inc_response>" and "<length>" and "<equals>"
    Given I have response <inc_response>
    And I have inc_db <inc_db>
    When I call read_all_files
    Given I have length <length>
    Then I should see read_all_files <equals>

  Examples:
    | inc_db |  inc_response | length | equals |
    | 0      |  0            | 6      | True   |
    | 0      |  1            | 6      | True   |
    | 1      |  1            | 8      | True   |
    | 1      |  0            | 7      | True   |
