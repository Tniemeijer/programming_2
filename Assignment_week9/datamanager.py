from sklearn.preprocessing import StandardScaler

class DataManager:
    def __init__(self):
        self.scaler = StandardScaler

    def preprocess(self, data):
        scaler = self.scaler()
        data = data.iloc[:,:-1]
        data = data.fillna(data.mean())
        data = scaler.fit_transform(data)
        return data
