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


def read_all_csv(datapath):
    csv_dict = {}
    for path, directories, files in os.walk(datapath):
        for file in files:
            if ".csv" in file:
                print(file)
                string_file = str(datapath+'/'+file)
                print(string_file)
                df = pd.read_csv(string_file)
                csv_dict[file] = df

                print(df.head())


if __name__ == '__main__':
    data_path = os.getcwd() + '/data'
    read_all_csv(data_path)







# When you have completed steps 1 and 2 detailed above.


## Step 3 call to training fnction mml.fit(sqlite_db_file, sqlite_training_table_name)

##  Step 4 call to test function mml.test(sqlite_db_file, sqlite_test_table_name)


