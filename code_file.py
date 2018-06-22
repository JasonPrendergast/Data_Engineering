#  Thanks for your interest in joining Mudano.  This
#  python 3 coding file aims to walkthrough a simulated
#  machine learning excercise but from a Data Engineer's
#  point of view.

#  Summary:
#  You are provided a series of data structures containing data points
#  about the acccidents on UK roads.  Most of these data structures are
#  in csv file format, however two structures are provided as a sqlite
#  db tables.  Your task is to 

# Steps to complete:
# 1. Bring all of these data structures together into one structure, keyed on accident_index.
# 2. Split the data into two sqlite table (80% - Training Data;20%  - Test Data)
# 3. Send the training data table as an argument to mml.fit() function.
# 4. Send test data table as an argument to mml.test() function.

#  Please note:
# 1. Please use comments liberally, this is reviewed by one of our data engineers.
# 2. mml.fit() function requires pandas, please ensure that it is available in env.
# 3. For simplicity, assume the db, csv and mml library files are in current working direcotry.
# 4. Comment about what you'd like to change if you had more control.
# 5. Ask questions!  If you see there is something wrong about data, please get in touch.

# All the best!

import sqlite3
import mml
import pandas as pd
import sklearn
import os
import argparse


def read_all_csv(datapath, inc_db, inc_response):
    # create empty dictionary
    csv_dict = {}
    # walk through the data file
    for path, directories, files in os.walk(datapath):
        # Grab all the files
        for file in files:
            # check the file extension for csv
            if ".csv" in file:
                # file the dataframe with the content of the csv
                df = pd.read_csv(datapath+'/'+file)
                print(file)
                # print(df.head())
                print(df.count())
                if df.empty:
                    print(file)
                # add the csv to the dictionary
                csv_dict[file] = df
            # check the file extension for db
            if inc_db != '0':
                if '.db' in file:
                    cnx = sqlite3.connect(datapath+'/'+file)
                    c = cnx.cursor()
                    table_names = find_all_table_names(c)
                    for table in table_names:
                        table = str(table)
                        for ch in [',', '-', ')', '(', '/', '\\', '[', ']', '{', '}', '&', '#', '\'', '"', ':', '', ')',
                                   '(', '*', '&',
                                   '^', '%', '$', '£', '@', '"', '!', '?', '.', '=', '+', '_', '']:
                            if ch in table:
                                table = table.replace(ch, "")

                        if table != 'response':
                            db_table = str(table) + '_' + file
                            csv_dict[db_table] = database_to_df(cnx, table)
                        elif table == 'response' and inc_response != '0':
                            db_table = str(table) + '_' + file
                            csv_dict[db_table] = database_to_df(cnx, table)
                        else:
                            print('no output')
    return csv_dict


def merge_dataframe_list(df_dict):
    # create a placeholder
    merged_df = None
    # loop the dictionary
    for df in df_dict.values():
        # check if the placeholder is none aka this is the first iteration
        if merged_df is None:
            # since it is the first iteration make the placeholder contain the first dataframe
            merged_df = df
        # if it is not the first loop
        else:
            merged_df = pd.merge(merged_df, df, on='Accident_Index', how='outer')
    return merged_df


def database_to_df(cnx, table):

    # get all the data from the table
    df = pd.read_sql_query("SELECT * FROM " + table, cnx)
    # print(list(df.columns.values))
    df = df.rename(columns={'acc_i': 'Accident_Index'})
    # print(df.head())
    print(table)
    print(df.count())

    # change the pk to column name to Accident_Index
    return df


def find_all_table_names(c):
    # get all tables in the database
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = c.fetchall()
    print(table_names)
    return table_names


def create_csv():
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--include_db', type=str, default='0',
                        help='Would you like to include db files set to 0 for no ')
    parser.add_argument('--include_response_table',
                        help="Would you like to include this erroneous table? set to 0 for no",
                        type=str,
                        default='0')
    args = parser.parse_args()
    inc_db = args.include_db
    inc_response = args.include_response_table

    data_path = os.getcwd() + '/data'
    data_frame_dict = read_all_csv(data_path, inc_db, inc_response)
    csv_merged = merge_dataframe_list(data_frame_dict)
    print('----------final---------------')
    print(csv_merged.count())









# When you have completed steps 1 and 2 detailed above.


## Step 3 call to training fnction mml.fit(sqlite_db_file, sqlite_training_table_name)

##  Step 4 call to test function mml.test(sqlite_db_file, sqlite_test_table_name)


