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

import mml
import pandas as pd
import os
import argparse
import handleoutputs
import produceoutput
from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    # use args parse to turn off and on db tables
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--include_db', type=str, default='1',
                        help='Would you like to include db files set to 0 for no ')
    parser.add_argument('--include_response_table',
                        help="Would you like to include this erroneous table? set to 0 for no",
                        type=str,
                        default='0')
    args = parser.parse_args()
    inc_db = args.include_db
    inc_response = args.include_response_table


    # Get the director path
    data_path = os.getcwd()+'/inputs'
    print(data_path)
    ProduceOutput = produceoutput.ProduceOutput()
    csv_merged = ProduceOutput.process_input_data(data_path, inc_db, inc_response)
    # use sklearn's built in train test split
    train, test = train_test_split(csv_merged, test_size=0.2)
    # convert the numpy arrays back to pandas dataframes
    train = pd.DataFrame(train)
    test = pd.DataFrame(test)
    # create handle output object
    HandleOutputs = handleoutputs.HandleOutputs()
    # insert the train test dataframes in to a new database
    HandleOutputs.data_frame_to_db('train', train)
    HandleOutputs.data_frame_to_db('test', test)

# When you have completed steps 1 and 2 detailed above.

## Step 3 call to training fnction mml.fit(sqlite_db_file, sqlite_training_table_name)
    output_train = mml.fit(os.getcwd() + '/data/traintest.db', 'train')
    print(output_train)
##  Step 4 call to test function mml.test(sqlite_db_file, sqlite_test_table_name)
    output_test = mml.test(os.getcwd() + '/data/traintest.db', 'test')
    print(output_test+output_train)

