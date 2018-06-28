import pandas as pd
import os

import sqlite3


class HandleInputs:
    def read_all_files(self, datapath, inc_db, inc_response, dbobj):
        try:
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
                            table_names = dbobj.find_all_table_names(c)
                            # loop the tables
                            csv_dict = dbobj.handle_all_tables(table_names, file, csv_dict, cnx, inc_response)
                            c.close()
                            cnx.close()
        except Exception as ex:
            print(ex)

        return csv_dict

    def merge_dataframe_list(self, df_dict):
        try:
            # create a placeholder
            merged_df = None
            # loop the dictionary
            for key, df in df_dict.items():
                # check if the placeholder is none aka this is the first iteration
                if merged_df is None:
                    # since it is the first iteration make the placeholder contain the first dataframe
                    merged_df = df
                # if it is not the first loop
                else:
                    try:
                        merged_df = pd.merge(merged_df, df, on='Accident_Index', how='outer', suffixes=('', '_'+key))
                    except Exception as ex:
                        pass
        except Exception as ex:
            print(ex)


        return merged_df
