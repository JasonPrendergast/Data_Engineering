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
from sklearn.model_selection import train_test_split

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
                if df.empty:
                    print(file)
                # add the csv to the dictionary
                csv_dict[file] = df
            # check if the db is required
            if inc_db != '0':
                # check the file extension for db
                if '.db' in file:
                    # Create database connection
                    cnx = sqlite3.connect(datapath+'/'+file)
                    c = cnx.cursor()
                    # Get the table names from the database
                    table_names = find_all_table_names(c)
                    # loop the tables
                    for table in table_names:
                        # turn the tuple to a string
                        table = str(table)
                        #clean the table name string
                        for ch in [',', '-', ')', '(', '/', '\\', '[', ']', '{', '}', '&', '#', '\'', '"', ':', '', ')',
                                   '(', '*', '&',
                                   '^', '%', '$', '£', '@', '"', '!', '?', '.', '=', '+', '_', '']:
                            if ch in table:
                                table = table.replace(ch, "")
                        # check if the table name is response
                        if table != 'response':
                            # create the dict key from the table name and file name
                            db_table = str(table) + '_' + file
                            # get the contents of the table and insert it into the dict with the key
                            csv_dict[db_table] = database_to_df(cnx, table)
                        # check if the table is response
                        elif table == 'response' and inc_response != '0':
                            # create the dict key from the table name and file name
                            db_table = str(table) + '_' + file
                            # get the contents of the table and insert it into the dict with the key
                            csv_dict[db_table] = database_to_df(cnx, table)
                        else:
                            # simple handle when response is bring skipped
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
    # change the pk to column name to Accident_Index
    return df


def find_all_table_names(c):
    # get all tables in the database
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = c.fetchall()
    return table_names


def create_csv():
    pass


def data_frame_to_db(name, data):
    conn = sqlite3.connect(os.getcwd()+'/data/'+'traintest.db')
    # c = conn.cursor()
    data.to_sql(name, con=conn, if_exists='replace')




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

    data_path = os.getcwd()
    data_frame_dict = read_all_csv(data_path, inc_db, inc_response)
    csv_merged = merge_dataframe_list(data_frame_dict)

    train, test = train_test_split(csv_merged, test_size=0.2)

    train = pd.DataFrame(train)
    test = pd.DataFrame(test)

    data_frame_to_db('train', train)
    data_frame_to_db('test', test)
    outputtrain = mml.fit(os.getcwd()+'/data/'+'traintest.db', 'train')
    print(outputtrain)
    outputtest = mml.test(os.getcwd()+'/data/'+'traintest.db', 'test')
    print(outputtest+outputtrain)

# When you have completed steps 1 and 2 detailed above.

## Step 3 call to training fnction mml.fit(sqlite_db_file, sqlite_training_table_name)

##  Step 4 call to test function mml.test(sqlite_db_file, sqlite_test_table_name)


