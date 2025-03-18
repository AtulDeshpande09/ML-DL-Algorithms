import numpy as np

class RobustScaler:

    def __init__(self):
        
        self.x_median = None
        self.x_iqr = None
    
    def fit(self,X:np.ndarray)->None:
        """
        This method finds mean , max and min of X
        X --> Array like data structure

        Return --> None
        """
        x = np.array(X)

        self.x_median = np.median(x)

        q1 = np.percentile(x , 25)
        q3 = np.percentile(x , 75)

        self.x_iqr = q3 - q1

    def fit_transform(self,X:np.ndarray):
        """
        Scales data using formula :
        X_scaled = (X - X_median)/IQR

        Return -> Array Like data Structure
        """

        self.fit(X)

        X_scaled:np.ndarray = np.array([ (x - self.x_median)/(self.x_median) for x in X ])

        return X_scaled

    def inverse_transform(self, X_scaled:list)->list:
        """
        Reverts Scaled data to Original Data

        Return --> list , nparray
        """

        X_original:np.ndarray = np.array([x*(self.x_iqr) + self.x_median for x in X_scaled ])

        return X_original



if __name__ == '__main__':
    print("Here is example : \n")
    x = [40,30,45,20,45,33,21,25,55,56,66]
    print("Data to be Scaled : ",x)

    scaler = RobustScaler()

    x_scaled = scaler.fit_transform(x)
    print("Scaled Data : ",x_scaled)
    print("\n")
