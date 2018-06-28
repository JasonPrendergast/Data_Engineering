from behave import given, then, when
import handleoutputs
import produceoutput
import handleinputs
import handleinputsdb
import sqlite3
import os
import pandas as pd


@given('I create new HandleinputDB_database_to_df context variables')
def i_create_new_HandleinputDB_database_to_df_context_variables(context):
    context.data_path = os.path.dirname(os.getcwd()) + '/inputs'
    context.cnx = sqlite3.connect(context.data_path + '/' + 'de.db')


@given('I have table {dbtable}')
def i_have_table(context, dbtable):
    context.dbtable = dbtable


@when('I call database_to_df')
def i_call_database_to_df(context):
    HandleInputDbobj = handleinputsdb.HandleInputDb()
    context.table_data_frame = HandleInputDbobj.database_to_df(context.cnx, context.dbtable)
    context.cnx.close()


@then('I should see database_to_df {equals}')
def i_should_see_database_to_df_result(context, equals):
    if context.table_data_frame is not None:
        if context.table_data_frame.empty:
            answer = False
        else:
            answer = True
    else:
        answer = False
    assert equals == str(answer)


# --------------------------------------------------------------------------------------------------------------------

@given('I create new HandleinputDB_find_all_tables_names context variables')
def i_create_new_HandleinputDB_find_all_tables_names_context_variables(context):
    context.data_path = os.path.dirname(os.getcwd()) + '/inputs' #os.getcwd() + '/inputs'
    context.cnx = sqlite3.connect(context.data_path + '/' + 'de.db')
    context.c = context.cnx.cursor()


@when('I call find_all_tables_names')
def i_call_find_all_tables_names(context):
    HandleInputDbobj = handleinputsdb.HandleInputDb()
    context.all_db_tables = HandleInputDbobj.find_all_table_names(context.c)
    context.c.close()
    context.cnx.close()


@then('I should see find_all_tables_names {equals}')
def i_should_see_find_all_tables_names_result(context, equals):
    if len(context.all_db_tables) == 2:
        answer = True
    else:
        answer = False
    assert equals == str(answer)

# ----------------------------------------------------------------------------------------------------------


@given('I create new HandleinputDB_handle_all_tables context variables')
def i_create_new_HandleinputDB_handle_all_tables_context_variables(context):
    context.data_path = os.path.dirname(os.getcwd()) + '/inputs' #os.path.dirname(os.getcwd()) + '/inputs'
    context.cnx = sqlite3.connect(context.data_path + '/' + 'de.db')
    context.csv_dict = {}


@given('I have names table {table_name1} {table_name2}')
def i_have_table(context, table_name1, table_name2):
    context.all_tables = {table_name1, table_name2}


@given('I have file name {file}')
def i_have_file_name(context, file):
    context.filename = file


@given('I have response {inc_response}')
def i_have_response(context, inc_response):
    context.inc_response = inc_response


@when('I call handle_all_tables')
def i_call_handle_all_tables(context):
    HandleInputDbobj = handleinputsdb.HandleInputDb()
    context.csv_dict = HandleInputDbobj.handle_all_tables(context.all_tables,
                                                               context.filename,
                                                               context.csv_dict,
                                                               context.cnx,
                                                               context.inc_response)
    context.cnx.close()


@then('I should see handle_all_tables {equals}')
def i_should_see_handle_all_tables_result(context, equals):
    firstkey = str(list(context.csv_dict.keys())[0])
    if context.csv_dict[firstkey] is not None:
        if len(context.csv_dict) > 0:
            answer = True
        else:
            answer = False
    else:
        answer = False
    assert equals == str(answer)

# ----------------------------------------------------------------------------------------------------------------


@given('I create new Handleinput_read_all_files context variables')
def i_create_new_Handleinput_handle_all_tables_context_variables(context):
    context.HandleInputDbobj = handleinputsdb.HandleInputDb()
    context.data_path = os.path.dirname(os.getcwd()) + '/inputs'


@given('I have inc_db {inc_db}')
def i_have_inc_db(context, inc_db):
    context.inc_db = inc_db


@when('I call read_all_files')
def i_call_read_all_files(context):
    # Create the handle inputs object
    HandleInputs = handleinputs.HandleInputs()
    # Run the handle inputs method read all
    context.data_frame_dict = HandleInputs.read_all_files(context.data_path,
                                                          context.inc_db,
                                                          context.inc_response,
                                                          context.HandleInputDbobj)


@given('I have length {length}')
def i_have_length(context, length):
    context.length = int(length)


@then('I should see read_all_files {equals}')
def i_should_see_read_all_files_result(context, equals):
    if len(context.data_frame_dict) == context.length:
        answer = True
    else:
        answer = False
    assert equals == str(answer)

# ----------------------------------------------------------------------


@given('I create new Handleinput_merge_dataframe_list context variables')
def i_create_new_Handleinput_merge_dataframe_list_context_variables(context):

    context.df_dict = {}

# When I call merge_dataframe_list
#     Then I should see merge_dataframe_list <equals>

# I have columns <Columnname1> <Columnname2> <Columnname3> <Columnname4>
# <Columnvalue1> <Columnvalue2> <Columnvalue3> <Columnvalue4>
# <Columnkey1> <Columnkey2> <Columnkey3> <Columnvkey4>

@given('I have columns {Columnname1} {Columnname2} {Columnname3} {Columnname4} {Columnvalue1} {Columnvalue2} {Columnvalue3} {Columnvalue4} {Columnvalue5} {Columnvalue6} {Columnkey1} {Columnkey2} {Columnkey3} {Columnvkey4}')
def i_have_columns(context, Columnname1, Columnname2, Columnname3, Columnname4,
                  Columnvalue1, Columnvalue2, Columnvalue3, Columnvalue4, Columnvalue5, Columnvalue6,
                  Columnkey1, Columnkey2, Columnkey3, Columnvkey4):
    data1 = [[Columnkey1, Columnvalue1], [Columnkey2, Columnvalue2], [Columnkey3, Columnvalue3]]
    df1 = pd.DataFrame(data1, columns=[Columnname1, Columnname2])
    data2 = [[Columnkey1, Columnvalue4], [Columnkey2, Columnvalue5], [Columnkey3, Columnvalue6]]
    df2 = pd.DataFrame(data2, columns=[Columnname3, Columnname4])
    dataname1 = 'dataname1'
    dataname2 = 'dataname2'
    context.df_dict = {dataname1: df1, dataname2: df2}

@when('I call merge_dataframe_list')
def i_call_merge_dataframe_list(context):
    # Create the handle inputs object
    HandleInputs = handleinputs.HandleInputs()
    # Run merge all the dataframes in dict to a single dataframe
    context.csv_merged = HandleInputs.merge_dataframe_list(context.df_dict)

@then('I should see merge_dataframe_list {equals}')
def i_should_see_merge_dataframe_list_result(context, equals):
    len(list(context.csv_merged.columns.values))
    if len(list(context.csv_merged.columns.values)) == 3:
        answer = True
    else:
        answer = False
    assert equals == str(answer)
# ---------------------------------------------------------------------------------------

@given('I create new HandleOutputs_data_frames_to_db context variables')
def i_create_new_HandleOutputs_data_frames_to_db_context_variables(context):
    context.data_path = os.path.dirname(os.getcwd()) + '/data'  # os.path.dirname(os.getcwd()) + '/inputs'
    context.cnx = sqlite3.connect(context.data_path + '/' + 'testing.db')
    context.csv_dict = {}
    context.df = None
    context.all_tables = {'mergedcsv'}
    context.filename = 'test'
    context.inc_response = 0

 # When I call data_frames_to_dbt
 #    Then I should see data_frames_to_db <equals>

@when('I call data_frames_to_dbt')
def i_call_data_frames_to_dbt_list(context):
    # Create the handle output object
    HandleOutputs = handleoutputs.HandleOutputs()
    # insert the dataframes in to a new database

    len(list(context.csv_merged.columns.values))
    HandleOutputs.data_frame_to_db('mergedcsv', context.csv_merged, context.cnx)

@then('I should see data_frames_to_db {equals}')
def i_should_see_data_frames_to_db_result(context, equals):
    len(list(context.csv_merged.columns.values))
    context.csv_dict
    firstkey = str(list(context.csv_dict.keys())[0])

    table_content = context.csv_dict[firstkey]
    print(table_content)
    context.cnx.close()
    # if len(list(context.csv_merged.columns.values)) == 3:
    #     answer = True
    # else:
    #     answer = False
    # assert equals == str(answer)