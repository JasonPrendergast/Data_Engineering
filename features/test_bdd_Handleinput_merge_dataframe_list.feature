
Feature: test cases Handleinput_merge_dataframe_list
  #background will run before every scenario
  Background: Create Handleinput_merge_dataframe_list context variables
    Given I create new Handleinput_merge_dataframe_list context variables
# datapath, inc_db, inc_response, dbobj
  Scenario Outline:  "<Columnname1>" and "<Columnname2>" and "<Columnname3>" and "<Columnname4>" and "<Columnvalue1>"and "<Columnvalue2>" and "<Columnvalue3>" and "<Columnvalue4>" and "<Columnkey1>"and "<Columnkey2>" and "<Columnkey3>" and "<Columnvkey4>" and "<equals>"
    Given I have columns <Columnname1> <Columnname2> <Columnname3> <Columnname4> <Columnvalue1> <Columnvalue2> <Columnvalue3> <Columnvalue4> <Columnvalue5> <Columnvalue6> <Columnkey1> <Columnkey2> <Columnkey3> <Columnkey4>
    When I call merge_dataframe_list
    Then I should see merge_dataframe_list <equals>

  Examples:
   | Columnname1    | Columnname2 | Columnname3    |Columnname4|Columnvalue1|Columnvalue2|Columnvalue3|Columnvalue4|Columnvalue5|Columnvalue6|Columnkey1|Columnkey2|Columnkey3|Columnkey4| equals |
   | Accident_Index | age         | Accident_Index | height    |  10        | 11         | 12         | 110        |120         |100         | 2100     |2111      |2333      |2450      | True   |
   | Accident_Index | age         | blah           | height    |  10        | 11         | 12         | 110        |120         |100         | 2100     |2111      |2333      |2450      | False  |