"""
excersise 1 jsonmaker
"""

import pandas as pd

class JsonMaker:
    """
    creates data json
    """

    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def read_file(self):
        file_df = pd.read_csv(self.path)
        return file_df
    
    def convert_to_json(self, df):
        match self.mode[0]:
            case "all":
                return df.T.to_json()
            case _:
                match len(self.mode):
                    case 1:
                        return df[df["Year"] == self.mode[0]].T.to_json()
                    case 2:
                        return df[df["Year"].between(self.mode[0],self.mode[1])].T.to_json()
    
    def read_convert(self):
        return self.convert_to_json(self.read_file())