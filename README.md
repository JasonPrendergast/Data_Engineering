# Use code_file

    \Data_Engineer_Assignment__1_\pip install -r requirements.txt
    
    \Data_Engineer_Assignment__1_\python code_file.py --include_db=0 --include_response_table=0
    \Data_Engineer_Assignment__1_>python code_file.py --include_db=1 --include_response_table=0
# Use behave

    \Data_Engineer_Assignment__1_\features>behave

#Behave results

Many more tests can be added but this is just a demonstration 

    Feature: test cases HandleOutputs_data_frames_to_db # test_bdd_HandleOutputs_data_frames_to_db.feature:2

      Background: Create HandleOutputs_data_frames_to_db context variables  # test_bdd_HandleOutputs_data_frames_to_db.feature:4

      Scenario Outline: "Accident_Index" and "age" and "blah" and "height" and "10"and "11" and "12" and "110" and "2100"and "2111" and "2333" and "<Columnvkey4>" and "False" -- @1.1   # test_bdd_HandleOutputs_data_frames_to_db.feature:16
        Given I create new HandleOutputs_data_frames_to_db context variables                                                                                                             # ../steps/steps.py:198
        Given I have columns Accident_Index age blah height 10 11 12 110 120 100 2100 2111 2333 2450                                                                                     # ../steps/steps.py:169
        When I call merge_dataframe_list                                                                                                                                                 # ../steps/steps.py:181
        And I call data_frames_to_dbt                                                                                                                                                    # ../steps/steps.py:212
        And I call handle_all_tables                                                                                                                                                     # ../steps/steps.py:91
        Then I should see data_frames_to_db False                                                                                                                                        # ../steps/steps.py:222
    
      Scenario Outline: "Accident_Index" and "age" and "Accident_Index" and "height" and "10"and "11" and "12" and "110" and "2100"and "2111" and "2333" and "<Columnvkey4>" and "True" -- @1.2   # test_bdd_HandleOutputs_data_frames_to_db.feature:17
        Given I create new HandleOutputs_data_frames_to_db context variables                                                                                                                      # ../steps/steps.py:198
        Given I have columns Accident_Index age Accident_Index height 10 11 12 110 120 100 2100 2111 2333 2450                                                                                    # ../steps/steps.py:169
        When I call merge_dataframe_list                                                                                                                                                          # ../steps/steps.py:181
        And I call data_frames_to_dbt                                                                                                                                                             # ../steps/steps.py:212
        And I call handle_all_tables                                                                                                                                                              # ../steps/steps.py:91
        Then I should see data_frames_to_db True                                                                                                                                                  # ../steps/steps.py:222
    
    Feature: test cases HandleinputDB_database_to_df # test_bdd_HandleinputDB_database_to_df.feature:2
    
      Background: Create HandleinputDB_database_to_df context variables  # test_bdd_HandleinputDB_database_to_df.feature:4
    
      Scenario Outline: "police"  and "True" -- @1.1                      # test_bdd_HandleinputDB_database_to_df.feature:14
        Given I create new HandleinputDB_database_to_df context variables # ../steps/steps.py:11
        Given I have table police                                         # ../steps/steps.py:17
        When I call database_to_df                                        # ../steps/steps.py:22
        Then I should see database_to_df True                             # ../steps/steps.py:29
    
      Scenario Outline: "response"  and "True" -- @1.2                    # test_bdd_HandleinputDB_database_to_df.feature:15
        Given I create new HandleinputDB_database_to_df context variables # ../steps/steps.py:11
        Given I have table response                                       # ../steps/steps.py:17
        When I call database_to_df                                        # ../steps/steps.py:22
        Then I should see database_to_df True                             # ../steps/steps.py:29
    
      Scenario Outline: "Not_a_table"  and "False" -- @1.3                # test_bdd_HandleinputDB_database_to_df.feature:16
        Given I create new HandleinputDB_database_to_df context variables # ../steps/steps.py:11
        Given I have table Not_a_table                                    # ../steps/steps.py:17
        When I call database_to_df                                        # ../steps/steps.py:22
        Then I should see database_to_df False                            # ../steps/steps.py:29
    
    Feature: test cases HandleinputDB_find_all_tables_names # test_bdd_HandleinputDB_find_all_tables_names.feature:2
    
      Background: Create HandleinputDB_find_all_tables_names context variables  # test_bdd_HandleinputDB_find_all_tables_names.feature:4
    
      Scenario Outline: no params and True -- @1.1                               # test_bdd_HandleinputDB_find_all_tables_names.feature:13
        Given I create new HandleinputDB_find_all_tables_names context variables # ../steps/steps.py:43
        When I call find_all_tables_names                                        # ../steps/steps.py:50
        Then I should see find_all_tables_names True                             # ../steps/steps.py:58
    
    Feature: test cases HandleinputDB_handle_all_tables # test_bdd_HandleinputDB_handle_all_tables.feature:2
    
      Background: Create HandleinputDB_handle_all_tables context variables  # test_bdd_HandleinputDB_handle_all_tables.feature:4
    
      Scenario Outline: "police"  and "police" and "test" and "0"and "True" -- @1.1   # test_bdd_HandleinputDB_handle_all_tables.feature:16
        Given I create new HandleinputDB_handle_all_tables context variables          # ../steps/steps.py:69
        Given I have names table police police                                        # ../steps/steps.py:76
        And I have file name test                                                     # ../steps/steps.py:81
        And I have response 0                                                         # ../steps/steps.py:86
        When I call handle_all_tables                                                 # ../steps/steps.py:91
        Then I should see handle_all_tables True                                      # ../steps/steps.py:104
    
      Scenario Outline: "police"  and "police" and "test" and "1"and "True" -- @1.2   # test_bdd_HandleinputDB_handle_all_tables.feature:17
        Given I create new HandleinputDB_handle_all_tables context variables          # ../steps/steps.py:69
        Given I have names table police police                                        # ../steps/steps.py:76
        And I have file name test                                                     # ../steps/steps.py:81
        And I have response 1                                                         # ../steps/steps.py:86
        When I call handle_all_tables                                                 # ../steps/steps.py:91
        Then I should see handle_all_tables True                                      # ../steps/steps.py:104
    
      Scenario Outline: "''"  and "''" and "test" and "1"and "False" -- @1.3   # test_bdd_HandleinputDB_handle_all_tables.feature:18
        Given I create new HandleinputDB_handle_all_tables context variables   # ../steps/steps.py:69
        Given I have names table '' ''                                         # ../steps/steps.py:76
        And I have file name test                                              # ../steps/steps.py:81
        And I have response 1                                                  # ../steps/steps.py:86
        When I call handle_all_tables                                          # ../steps/steps.py:91
        Then I should see handle_all_tables False                              # ../steps/steps.py:104
    
    Feature: test cases Handleinput_merge_dataframe_list # test_bdd_Handleinput_merge_dataframe_list.feature:2
    
      Background: Create Handleinput_merge_dataframe_list context variables  # test_bdd_Handleinput_merge_dataframe_list.feature:4
    
      Scenario Outline: "Accident_Index" and "age" and "Accident_Index" and "height" and "10"and "11" and "12" and "110" and "2100"and "2111" and "2333" and "<Columnvkey4>" and "True" -- @1.1   # test_bdd_Handleinput_merge_dataframe_list.feature:14
        Given I create new Handleinput_merge_dataframe_list context variables                                                                                                                     # ../steps/steps.py:157
        Given I have columns Accident_Index age Accident_Index height 10 11 12 110 120 100 2100 2111 2333 2450                                                                                    # ../steps/steps.py:169
        When I call merge_dataframe_list                                                                                                                                                          # ../steps/steps.py:181
        Then I should see merge_dataframe_list True                                                                                                                                               # ../steps/steps.py:188
    
      Scenario Outline: "Accident_Index" and "age" and "blah" and "height" and "10"and "11" and "12" and "110" and "2100"and "2111" and "2333" and "<Columnvkey4>" and "False" -- @1.2   # test_bdd_Handleinput_merge_dataframe_list.feature:15
        Given I create new Handleinput_merge_dataframe_list context variables                                                                                                            # ../steps/steps.py:157
        Given I have columns Accident_Index age blah height 10 11 12 110 120 100 2100 2111 2333 2450                                                                                     # ../steps/steps.py:169
        When I call merge_dataframe_list                                                                                                                                                 # ../steps/steps.py:181
        Then I should see merge_dataframe_list False                                                                                                                                     # ../steps/steps.py:188
    
    Feature: test cases Handleinput_read_all_files # test_bdd_Handleinput_read_all_files.feature:2
    
      Background: Create Handleinput_read_all_files context variables  # test_bdd_Handleinput_read_all_files.feature:4
    
      Scenario Outline: "0" and "0" and "6" and "True" -- @1.1          # test_bdd_Handleinput_read_all_files.feature:16
        Given I create new Handleinput_read_all_files context variables # ../steps/steps.py:119
        Given I have response 0                                         # ../steps/steps.py:86
        And I have inc_db 0                                             # ../steps/steps.py:125
        When I call read_all_files                                      # ../steps/steps.py:130
        Given I have length 6                                           # ../steps/steps.py:141
        Then I should see read_all_files True                           # ../steps/steps.py:146
    
      Scenario Outline: "0" and "1" and "6" and "True" -- @1.2          # test_bdd_Handleinput_read_all_files.feature:17
        Given I create new Handleinput_read_all_files context variables # ../steps/steps.py:119
        Given I have response 1                                         # ../steps/steps.py:86
        And I have inc_db 0                                             # ../steps/steps.py:125
        When I call read_all_files                                      # ../steps/steps.py:130
        Given I have length 6                                           # ../steps/steps.py:141
        Then I should see read_all_files True                           # ../steps/steps.py:146
    
      Scenario Outline: "1" and "1" and "8" and "True" -- @1.3          # test_bdd_Handleinput_read_all_files.feature:18
        Given I create new Handleinput_read_all_files context variables # ../steps/steps.py:119
        Given I have response 1                                         # ../steps/steps.py:86
        And I have inc_db 1                                             # ../steps/steps.py:125
        When I call read_all_files                                      # ../steps/steps.py:130
        Given I have length 8                                           # ../steps/steps.py:141
        Then I should see read_all_files True                           # ../steps/steps.py:146
    
      Scenario Outline: "1" and "0" and "7" and "True" -- @1.4          # test_bdd_Handleinput_read_all_files.feature:19
        Given I create new Handleinput_read_all_files context variables # ../steps/steps.py:119
        Given I have response 0                                         # ../steps/steps.py:86
        And I have inc_db 1                                             # ../steps/steps.py:125
        When I call read_all_files                                      # ../steps/steps.py:130
        Given I have length 7                                           # ../steps/steps.py:141
        Then I should see read_all_files True                           # ../steps/steps.py:146
    
    6 features passed, 0 failed, 0 skipped
    15 scenarios passed, 0 failed, 0 skipped
    77 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m9.902s
        
# Data_Engineer_Assignment__1_

DATA ENGINEER RECRUITMENT STAGE 2 INFORMATION

Many thanks for your continued interest in joining Mudano. To understand if you are a good fit for Mudano, and if we are a good fit for you we would like to work together on a test assignment. You should work with us in the style you anticipate you would if you already worked here. The assignment is as much about testing our ability to work together as it is testing your ability to produce great code and to check your understanding of data engineering issues. 

The work should be returned to us 2 days prior to your assignment interview. If this timeline isn’t feasible please let us know and we are happy to reschedule. We would be, of course, happy to receive earlier submissions.


Using AI to prevent deaths in car accidents

CONTEXT
When our brilliant data scientists crawl out of their maths caves and present their latest findings to the rest of the company. Everyone is in awe: some from amazement what the model can do and some—mostly engineers—are astonished and challenged as to how to put this new non-deterministic code into a performant, scalable production system.

Luckily, there is a hero that is coming to aid their naive data science brethren and sistren (that’s an actual word, btw). Enter, the data engineer.

In our scenario the data scientists have come up with a model that is helping prevent accidents on the road by forecasting the severity of an accident given some parameters. The rest is up to you!

REQUIREMENT OVERVIEW
The task below is split into two parts. The first tests your coding abilities in a data engineering context.

The second part is aimed at testing your understanding of how to evolve a prototype into a production system. 

This is not an exam or an academic exercise. The inputs and the process resemble the scenarios that could be encountered in real-life practical settings. Throughout an assignment. We expect you to communicate with us, ask questions and focus on getting to a fully working MVP and technical specifications. 

You will be provided with a data on all the road accidents in the UK. They have several columns indicating everything from where the accident is located to whether a police officer was present and accident severity. 

This data has been exported from several legacy systems and to the best knowledge of your Database Admin, it should be what you asked for, but it is always good to check. 

OBJECTIVES
(1) Reconstruct the data in memory (as per the steps below), feed this data through a model and then write out the result.
(2) Write up a technical document describing your view on a scope and high level architecture of this solution if it was to be implemented in a production setting (no more than 2 pages excluding diagrams). and what are some of the considerations to make this work for everyone in Mudano in the future.

Steps
For (1):
a. Install any dependencies
b. Create a Python script that does the following
Load the data sources for this assignment
Combine the data sources into a single dataset
Feed the combined dataset into the model learning procedure from machine_learning.py
Write the results as .CSV

For (2) we are intentionally not giving you any directions: capture anything you deem relevant. But also feel free to ask any questions!

OUR PROMISE TO YOU

This work should not take more than 5 hours of fully concentrated time. But any extra effort would surely be appreciated. 
This assignment should not require experience with any non-essential skills (see job spec for what those are).
This assignment should most accurately test the real-life data engineering scenarios.

RESOURCES
Following resources are a part of .zip file sent to you:
This document explaining this exercise.
mml.py One python wrapper loading from Scikit learn-like model (expected to install scikit if not present on their local environment).
data.zip Several data sources and a sqlite database.
code_file.py File where you should write your solution

QUESTIONS
If you would like further clarity of requirements or have any questions we would be happy to make time available - just ask! Please consider this activity as how you were working when part of the team already, and do feel comfortable working in your normal style. 
