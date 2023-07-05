"""
Anomaly detector- Assignment week 9

Detector that uses a pretrained unsupervised anomaly detection model
to predict outliers in new data.

Author: T.Niemeijer
Date: 2023/07/05
"""

#imported libraries
import joblib
import pandas as pd
import os
from time import sleep

#local modules
from datamanager import DataManager
from plotter import Plotter
from log import Logger

class Main:
    """
    Main class for running the automated anomaly detector

    --------------
    params:
            clf_path (str): path to the classifier, in .joblib format.
            data_path (str): path to where new data is coming in.
            output path (str): path where plots are stored.

    """
    def __init__(self, clf_path, data_path, output_path, interval=30):
        #initializing Main.
        self.classifier = joblib.load(clf_path)
        self.output_folder = output_path
        self.data_path = data_path
        self.queue = []
            #initializing the subclasses.
        self.log = Logger()
        self.datamanager = DataManager()
        self.plotter = Plotter()
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
        except IndexError:
            self.queue = []

    def _check_new_files(self, list_of_files):
        """
        Checks the availability of new files in the data folder.

        --------------
        """
        already_processed = list(set(self.log.done).intersection(set(list_of_files)))
        list_of_files = [file for file in list_of_files if file not in already_processed]
        self.log.add_to_log(f'New files found: {list_of_files}')
        return list_of_files

    def _preprocess(self):
        """
        Preprocesses the current data with the DataManager class
        It removes NA values and scales the data.

        --------------
        Output:
            overwrites self.data with preprocessed data
        """
        self.X = self.datamanager.preprocess(self.data)
        self.log.add_to_log(f'Preprocessing of {self.data_name} is finished')
    
    def _classify(self):
        """
        Uses a premade model to predict whether there are anomalies
        in the data.

        --------------
        Output:
            adds column ["pred"] with the predicted values to self.data
        """
        self.data["pred"] = self.classifier.predict(self.X)
        self.log.add_to_log(f'Finished outlier detection of {self.data_name}')
    
    def _plot(self, sensors=[10,20,30]):
        """
        Plots the anomaly whenever new data is available.

        --------------
        param:
               sensor (int): sensor number that is used for the plot.
        """
        # getting rid of the extension (.csv) [:-4]
        plot_path = f'{self.output_folder}/{self.data_name[:-4]}_plot'
        plot = self.plotter.sensor_plot(data=self.data, sensors=sensors)
        plot.savefig(plot_path)
        self.log.add_to_log(f'Plot saved as {plot_path}.png')

    def main(self):
        """
        main function, infinite loop.
        Checks if there is data in the queue and runs the process. 
        After finishing or when nothing is in the queue
         it will go to sleep for 30 secs.
        After that it will look for new data.
        """
        while True:
            self._check_data_available()
            while len(self.queue) > 0:
                self._get_new_data()
                self._preprocess()
                self._classify()
                self._plot()
                self.log.done.append(self.data_name)
            sleep(self.interval)
            


if __name__ == '__main__':
    clf_path = "/Users/timniemeijer/programming_2/Assignment_week9/loof_classifier.joblib"
    data_path = "/Users/timniemeijer/programming_2/Assignment_week9/DATA"
    output_path = "/Users/timniemeijer/programming_2/Assignment_week9/plots"
    main = Main(clf_path=clf_path, data_path=data_path, output_path=output_path)
    main.main()
            
            
        