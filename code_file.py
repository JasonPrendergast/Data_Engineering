import mml
import pandas as pd
import os
import argparse
import handleoutputs
import produceoutput
from sklearn.model_selection import train_test_split
import sqlite3


if __name__ == '__main__':
    # use args parse to turn off and on db tables
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


    # Get the director path
    data_path = os.getcwd()+'/inputs'

    # Create the merged data from the inputs
    ProduceOutput = produceoutput.ProduceOutput()
    csv_merged = ProduceOutput.process_input_data(data_path, inc_db, inc_response)

    # use sklearn's built in train test split
    train, test = train_test_split(csv_merged, test_size=0.2)

    # convert the numpy arrays back to pandas dataframes
    train = pd.DataFrame(train)
    test = pd.DataFrame(test)

    # create handle output object
    HandleOutputs = handleoutputs.HandleOutputs()

    # create data directory if it doesn't exist
    directory = os.getcwd() + '/data/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # make new connection to traintest db
    conn = sqlite3.connect(directory + 'traintest.db')

    # insert the train test dataframes in to a new database
    HandleOutputs.data_frame_to_db('train', train, conn)
    HandleOutputs.data_frame_to_db('test', test, conn)
    conn.close()

    HandleOutputs.create_csv('train', train, inc_db, inc_response)
    HandleOutputs.create_csv('test', test, inc_db, inc_response)

# When you have completed steps 1 and 2 detailed above.

## Step 3 call to training fnction mml.fit(sqlite_db_file, sqlite_training_table_name)
    output_train = mml.fit(os.getcwd() + '/data/traintest.db', 'train')
    print(output_train)
##  Step 4 call to test function mml.test(sqlite_db_file, sqlite_test_table_name)
    output_test = mml.test(os.getcwd() + '/data/traintest.db', 'test')
    print(output_test+output_train)

