"""
excersise 1 jsonmaker
"""

import pandas as pd

class JsonMaker:
    """
    creates data json
    """

    def __init__(self, path):
        self.path = path

    def read_file(self):
        file_df = pd.read_csv(self.path)
        return file_df
    
    def convert_to_json(self, df):
        json = df.T.to_json()
        return json
    
    def read_convert(self):
        return self.convert_to_json(self.read_file())