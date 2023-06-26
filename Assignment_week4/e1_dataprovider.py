"""
Dataprovider class excersise 1
"""

from  e1_jsonmaker import JsonMaker

class DataProvider:
    """
    Class that provides data
    """
    def __init__(self,param, path, jsonmaker=JsonMaker):
        self.mode = self.get_mode(param)
        self.jsonmaker = jsonmaker(path, self.mode)
        self.data = self.jsonmaker.read_convert()

    def get_mode(self, param):
        match len(param):
            case 1:
                match param[0]:
                    case "all":
                        return param
                    case _:
                        try:
                            r_val = int(param[0])
                            self.check_val(r_val)
                            return [r_val]
                        except Exception as exc:
                            raise ValueError from exc
            case 2:
                try:
                    r_val1 = int(param[0])
                    r_val2 = int(param[1])
                    if r_val1 > r_val2:
                        raise ValueError
                    return [r_val1,r_val2]
                except Exception as exc:
                    raise ValueError from exc
            case _:
                raise ValueError

    def check_val(self, val):
        if val < 1881 or val > 2021:
            raise ValueError
        