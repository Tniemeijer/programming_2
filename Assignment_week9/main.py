#imported libraries
import pickle
import pandas as pd
import os
import matplotlib.pyplot as plt
from time import sleep

#local modules
from datamanager import DataManager
from plotter import Plotter
from log import Logger

class Main:
    def __init__(self, clf_path, data_path, output_path, log_file):
        self.classifier = pickle.loads(clf_path)
        self.data_path = data_path
        self.datamanager = DataManager()
        self.plotter = Plotter
        self.output_folder = output_path
        self.log = Logger(log_file)
        self.queue = [] 
    
    def _check_data_available(self):
        """
        If there is a file in the folder that is not yet in the log
        schedule for processing pipeline in self.queue

        --------------
        Output:
            status (bool): if there is new data= True, else= False
                
            Add new files to self.queue


        """
        files = os.listdir(self.data_path)
        new_files = self.logger.check_new_files(files)
        self.queue.append(new_files)

    def _get_new_data(self):
        """
        Gets new data from the queue of data, removes data from queue
        and uses it.
        """
        new_file = self.queue.pop()
        self.data = pd.read_csv(new_file)
        self.data_name = new_file

    def _preprocess(self):
        """
        Preprocesses the current data with the DataManager class
        It removes NA values and scales the data.

        --------------
        Output:
            overwrites self.data with preprocessed data
        """
        self.data = self.datamanager.preprocess(self.data)
    
    def _classify(self):
        """
        Uses a premade model to predict whether there are anomalies
        in the data.

        --------------
        Output:
            adds column ["pred"] with the predicted values to self.data
        """
        self.data["pred"] = self.classifier.predict(self.data)
    
    def _plot(self, sensor):
        """
        Plots the anomaly 
        """
        plotter = plotter(data=self.data)
        plot = plotter.sensor_plot(sensor=sensor)
        plt.savefig(plot,f'{self.output}/{self.data_name}')

    def main(self):
        """
        main function, checks if there is data in the queue and
        runs the process. Otherwise it will look in the folder 
        """
        while True:
            while self.queue:
                self._get_new_data()
                self._preprocess()
                self._classify()
                self._plot()
            else:
                self._check_data_available()
                sleep(10)
        
            
            
        