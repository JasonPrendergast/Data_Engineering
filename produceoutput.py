import handleinputs
import handleinputsdb

class ProduceOutput:
    def process_input_data(self, data_path, inc_db, inc_response):
        # create handleinputdbobj
        HandleInputDbobj = handleinputsdb.HandleInputDb()
        # Create the handle inputs object
        HandleInputs = handleinputs.HandleInputs()
        # Run the handle inputs method read all
        data_frame_dict = HandleInputs.read_all_files(data_path, inc_db, inc_response, HandleInputDbobj)
        # Run merge all the dataframes in dict to a single dataframe
        csv_merged = HandleInputs.merge_dataframe_list(data_frame_dict)
        return csv_merged
