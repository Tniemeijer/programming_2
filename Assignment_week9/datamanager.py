from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

class DataManager:
    def __init__(self):
        self.scaler = StandardScaler
        self.pca = PCA(n_components=2)

    def preprocess(self, data):
        scaler = self.scaler()
        data = pd.DataFrame(data.iloc[:,1:-1]) # Magic numbers to drop time and classification columns
        data = data.fillna(data.mean())
        data = scaler.fit_transform(data)
        data = self.pca.fit_transform(data)
        return data
    
