import os


class Logger:
    def __init__(self, log_file):
        """
        Initializes the logger, checks whether the log file exists.
        If not, it creates the log file.
        """
        self.log = log_file

    def add_to_log(self, itm):
        """
        
        """
        with open(self.log_file, 'a') as log:
            log.writelines(itm)
    
    def check_new_files(self, list_of_files):
        with open(self.log,'r') as log:
            ref = log.read().splitlines()
        already_processed = list(set(ref).intersection(set(list_of_files)))
        list_of_files.remove(already_processed)
        return list_of_files


        