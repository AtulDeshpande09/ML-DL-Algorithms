import math

class Normalizer:

    def __init__(self):
        
        self.x_mean = None
        self.x_max = None
        self.x_min = None
    
    def fit(self,X:list)->None:
        """
        This method finds mean , max and min of X
        X --> Array like data structure

        Return --> None
        """

        self.x_mean = sum(X)/len(X) # calculates mean
        self.x_min = min(X)
        self.x_max = max(X)

    def fit_transform(self,X:list)->list:
        """
        Normalize data using formula :
        X_scaled = (X - X_mean)/ (Xmax - Xmin)

        Return -> Array Like data Structure
        """

        self.fit(X)

        X_scaled = [ (x - self.x_mean)/(self.x_max-self.x_min) for x in X ]

        return X_scaled

    def inverse_transform(self, X_scaled:list)->list:
        """
        Reverts Scaled data to Original Data

        Return --> list
        """

        X_original = [x*(self.x_max-self.x_min) + self.x_mean for x in X_scaled ]

        return X_original



if __name__ == '__main__':
    print("Here is example : \n")
    x = [40,30,45,20,45,33,21,25,55,56,66]
    print("Data to be Scaled : ",x)

    scaler = Normalizer()

    x_scaled = scaler.fit_transform(x)
    print("Scaled Data : ",x_scaled)
    print("\n")
