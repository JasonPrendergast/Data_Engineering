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
    context.data_path = os.getcwd() + '/inputs' #os.path.dirname(os.getcwd()) + '/inputs'
    print('-----------------')
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
            print('--------------------')
            print('1')
        else:
            answer = True
            print('--------------------')
            print('2')

    else:
        print('--------------------')
        print('3')

        answer = False
    print('--------------------')
    print(answer)
    assert equals == str(answer)
