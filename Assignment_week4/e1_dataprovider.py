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
        print(self.mode)
        self.data = self.jsonmaker.read_convert()

    def get_mode(self, param):
        match len(param):
            case 1:
                match param[0]:
                    case "all":
                        return param
                    case _:
                        try: 
                            return [int(param[0])]
                        except Exception as exc:
                            print(exc)
            case 2:
                try:
                    return [int(param[0]),int(param[1])]
                except Exception as exc:
                    print(exc)
            case _:
                raise ValueError