import pandas
import sqlite3
import os

class HandleOutputs:
    def create_csv(self, name, data):
        pass

    def data_frame_to_db(self, name, data):
        # create new database connection
        conn = sqlite3.connect(os.getcwd()+'/data/'+'traintest.db')
        # create a table and from the dataframe and insert the values
        data.to_sql(name, con=conn, if_exists='replace')
