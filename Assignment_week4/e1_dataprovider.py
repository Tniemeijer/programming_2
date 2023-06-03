"""
Dataprovider class excersise 1
"""

from  e1_jsonmaker import JsonMaker

class DataProvider:
    """
    Class that provides data
    """
    def __init__(self,param, path, jsonmaker=JsonMaker):
        self.jsonmaker = jsonmaker(path)
        self.mode = self.get_mode(param)
        self.data = self.jsonmaker.read_convert()

    def get_mode(self, param):
        if param == "all":
                return param
        else:
             raise ValueError
    
