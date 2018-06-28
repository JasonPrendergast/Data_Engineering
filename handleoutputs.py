import pandas
import sqlite3
import os

class HandleOutputs:
    def create_csv(self, name, data, inc_db, inc_response):
        try:
            complete_name = name + "inc_db_" + inc_db + '_inc_response_' + inc_response
            directory = os.getcwd() + '/output/' + complete_name

            if not os.path.exists(directory):
                os.makedirs(directory)
            data.to_csv(directory + '/' + name + '.csv')
        except Exception as ex:
            print(ex)




    def data_frame_to_db(self, name, data, conn):
        try:
            # create a table and from the dataframe and insert the values
            data.to_sql(name, con=conn, if_exists='replace')
        except Exception as ex:
            print(ex)

