# Good work. Nice in different classes and layers.
# A few small imnprovements are possible, but nothing terrible.

"""
Anomaly detector- Assignment week 9

Detector that uses a pretrained unsupervised anomaly detection model
to predict outliers in new data.

Author: T.Niemeijer
Date: 2023/07/05
"""

#standard libraries
import json
import os
import traceback
from time import sleep

#imported libraries
import joblib
import pandas as pd

#local modules
from datamanager import DataManager
from plotter import Plotter
from log import Logger

class AnomalyDetector:
    """
    Main class for running the automated anomaly detector

    

    """
    def __init__(self, classifier_path, data_path, output_img, 
                sensors, output_log_path, interval=30):
        """
        Initializes the AnomalyDetector

        --------------
        params:
            classifier_path (str): Path to the pretrained classifier model.
            data_path (str): Path to the directory where new data is stored.
            output_img_path (str): Path to the directory where plots are saved.
            sensors (list): List of sensor numbers used for plotting.
            output_log_path (str): Path to the log file.
            interval (int): Time interval in seconds between 
                            consecutive checks for new data.
        """
        #initializing Main.
        self.classifier = joblib.load(classifier_path)
        self.output_img= output_img
        self.data_path = data_path
        self.queue = []
            #initializing the subclasses.
        self.log = Logger(log_path=output_log_path)
        self.datamanager = DataManager()
        self.plotter = Plotter(sensors=sensors)
        self.interval = interval
        
    def _check_data_available(self):
        """
        If there is a file in the folder that is not yet in the log
        schedule for processing pipeline in self.queue

        --------------
        Output:
                
            Add new files to self.queue

        """
        #Only find .csv files.
        files = [file for file in os.listdir(self.data_path) if file.endswith('.csv')]
        new_files = self._check_new_files(files)
        self.queue = new_files

    def _get_new_data(self):
        """
        Gets new data from the queue of data, removes data from queue
        and uses it.
        """
        try:
            new_file = self.queue.pop()
            self.data = pd.read_csv(f'{self.data_path}/{new_file}')
            self.data_name = new_file
        except Exception:
            self.data = None
            error = traceback.format_exc() 
            self.log.add_to_log(itm=f'The following error occurred while\
                                     getting new data from the queue:\
                                    \n{str(error)}', mode='err')
            self.queue = []


    def _check_new_files(self, list_of_files):
        """
        Checks the availability of new files in the data folder.

        --------------
        """
        already_processed = list(set(self.log.done).intersection(set(list_of_files)))
        list_of_files = [file for file in list_of_files if file not in already_processed]
        if list_of_files:
            self.log.add_to_log(f'New files found: {list_of_files}')
        else:
            self.log.add_to_log('No new files found')
        return list_of_files

    def _preprocess(self):
        """
        Preprocesses the current data with the DataManager class
        It removes NA values and scales the data.

        --------------
        Output:
            overwrites self.data with preprocessed data
        """
        try: 
            self.X = self.datamanager.preprocess(self.data)
            self.log.add_to_log(f'Preprocessing of {self.data_name} is finished')
        except Exception:
            error = traceback.format_exc()
            self.X = None
            self.data = None
            self.log.add_to_log(itm=f'During preprocessing an error occurred:\
                \n{str(error)}', mode='err')

    
    def _classify(self):
        """
        Uses a premade model to predict whether there are anomalies
        in the data.

        --------------
        Output:
            adds column ["pred"] with the predicted values to self.data
        """
        try: 
            self.data["pred"] = self.classifier.predict(self.X)
            self.log.add_to_log(f'Finished outlier detection of {self.data_name}')
        except Exception:
            error = traceback.format_exc()
            self.log.add_to_log(itm=f'During preprocessing an error occurred:\
                \n{str(error)}', mode='err')

    def _plot(self):
        """
        Plots the anomaly whenever new data is available.

        --------------
        param:
               sensor (int): sensor number that is used for the plot.
        """
        # getting rid of the extension (.csv) [:-4]
        try:
            plot_path = f'{self.output_img}/{self.data_name[:-4]}_plot'
            plot = self.plotter.sensor_plot(data=self.data)
            plot.savefig(plot_path)
            self.log.add_to_log(f'Plot saved as {plot_path}.png')
        except Exception:
            error = traceback.format_exc()  # Get the formatted traceback as a string
            self.log.add_to_log(itm=f'During plotting an error occurred:\
                \n{error}', mode='err')

    def run(self):
        """
        main function, infinite loop.
        Checks if there is data in the queue and runs the process. 
        After finishing or when nothing is in the queue
         it will go to sleep for 30 secs.
        After that it will look for new data.
        """
        while True:
            self.log.add_to_log('Looking for new files')
            self._check_data_available()
            while len(self.queue) > 0:
                self._get_new_data()
                self._preprocess()
                self._classify()
                self._plot()
                self.log.done.append(self.data_name)
            self.log.add_to_log(f'Idle for {self.interval} seconds')
            sleep(self.interval)
            

if __name__ == '__main__':
    #clf_path = "/Users/timniemeijer/programming_2/Assignment_week9/loof_classifier.joblib"
    #data_path = "/Users/timniemeijer/programming_2/Assignment_week9/DATA"
    #output_path = "/Users/timniemeijer/programming_2/Assignment_week9/plots"
    with open("Assignment_week9/application.json",'r', encoding='utf8') as js_file:
        config = json.load(js_file)

    detector = AnomalyDetector(classifier_path=config["classifier"],
                data_path=config["input_dir"],
                output_img=config["output_img"],
                output_log_path=config["output_log"],
                sensors=config["sensors"],
                interval=config["interval"])
    detector.run()