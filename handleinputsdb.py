import pandas as pd

import os


class HandleInputDb:
    def database_to_df(self, cnx, table):
        df = None
        try:
            # get all the data from the table
            df = pd.read_sql_query("SELECT * FROM " + table, cnx)
            df = df.rename(columns={'acc_i': 'Accident_Index'})
            if table == 'police':
                df = df.rename(columns={'police_force': 'police_force_db'})
                df = df.rename(columns={'did_police_officer_attend_scene_of_accident':
                                            'did_police_officer_attend_scene_of_accident_db'})
            # change the pk to column name to Accident_Index
        except Exception as ex:
            pass
        if df is None:
            # this will cause an error later if it is triggered although it should never happen
            # because this is from a list of tables taken from the database. This will be triggered in testing
            pass
        else:
            return df

    def find_all_table_names(self, c):
        try:
            # get all tables in the database
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            table_names = c.fetchall()
        except Exception as ex:
            print(ex)
        return table_names

    def handle_all_tables(self, table_names, file, csv_dict, cnx, inc_response):
        try:
            # loop the tables
            for table in table_names:
                # turn the tuple to a string
                table = str(table)

                # clean the table name string
                for ch in [',', '-', ')', '(', '/', '\\', '[', ']', '{', '}', '&', '#', '\'', '"', ':', '', ')',
                           '(', '*', '&',
                           '^', '%', '$', '£', '@', '"', '!', '?', '.', '=', '+', '']:
                    if ch in table:
                        table = table.replace(ch, "")

                # create the dict key from the table name and file name
                db_table = str(table) + '_' + file

                # check if the table name is response
                if table != 'response':

                    # get the contents of the table and insert it into the dict with the key
                    csv_dict[db_table] = self.database_to_df(cnx, table)

                # check if the table is response
                elif table == 'response' and inc_response != '0':

                    # get the contents of the table and insert it into the dict with the key
                    csv_dict[db_table] = self.database_to_df(cnx, table)
                else:
                    # simple handle when response is bring skipped
                    pass
        except Exception as ex:
            print(ex)
        return csv_dict
