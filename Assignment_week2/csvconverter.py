"""
Class that converts a csv to a .json format
"""
import json
import linecache as lc

class CsvConverter:
    """converts .csv to .json"""
    def __init__(self, csv_path):
        self.header = self.get_header(csv_path)

    def get_header(self, csv_path):
        """Returns header of the .csv file in a list()"""
        first_line = lc.getline(csv_path, 1)
        header = first_line.strip().split(",")
        return header

    def csv_to_json(self, lines):
        """
        A section of lines will be fed to this function
        the function splits and returns the lines
        in .json format
        """
        json_file = []
        for line in lines:
            line = line.strip().split(",")
            try:
                assert len(self.header) == len(line) 
                json_file.append({h:line[c] for c,h in enumerate(self.header)})
            except Exception:
                if len(line) == 0:
                    json_file.append("")
                    return json.dumps(json)
                else:
                    #print(f"line {c+1} has not the right amount of values")
                    pass
        return json

