from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

class DataManager:
    """
    DataManager class to preprocess the data
    to be used by the outlier detection model.
    """
    def __init__(self):
        self.scaler = StandardScaler
        self.pca = PCA(n_components=2)

    def preprocess(self, data):
        """
        Preprocesses the data for further use in the prediction model.

        --------------

        params:
                data (pandas.Dataframe): Pandas sensor dataframe with 
                                        time, status and sensors in columns
                                        and values in the rows.

        output:
                data (pandas.Dataframe): Scaled (sklearn.StandardScaler) 
                            and sklearn.PCA reduced (n_components =2) dataframe. 
        """
        scaler = self.scaler()
        data = pd.DataFrame(data.iloc[:,1:-1]) # Magic numbers to drop time and classification columns
        data = data.fillna(data.mean())
        data = scaler.fit_transform(data)
        data = self.pca.fit_transform(data)
        return data
    
