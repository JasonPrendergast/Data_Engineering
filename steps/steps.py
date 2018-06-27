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
    context.data_path = os.path.dirname(os.getcwd()) + '/inputs' #os.getcwd() + '/inputs'

    print('------------------------')
    print(context.data_path)
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
    print(context.data_path)
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
    print(context.data_path)
    context.cnx = sqlite3.connect(context.data_path + '/' + 'de.db')
    context.csv_dict = {}


@given('I have names table {table_name1} {table_name2}')
def i_have_table(context, table_name1, table_name2):
    context.all_tables = {table_name1, table_name2}


@given('I have file name {file}')
def i_have_table(context, file):
    context.filename = file


@given('I have response {inc_response}')
def i_have_table(context, inc_response):
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

