import pandas
import sqlite3
import os

class HandleOutputs:
    def create_csv(self, name, data):
        pass

    def data_frame_to_db(self, name, data, conn):
        try:
            # create new database connection


            # create a table and from the dataframe and insert the values
            data.to_sql(name, con=conn, if_exists='replace')
        except Exception as ex:
            print(ex)
            pass
