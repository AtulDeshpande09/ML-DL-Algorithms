class OneHotEncoder:

    def __init__(self,data:list):
        self.data = data
        self.unique_labels = list(set(data))
        self.no_labels = len(self.unique_labels)
        self.encoded_dict = {label :[] for label in self.unique_labels}

    def fit_transform(self):
        for data_point in self.data:
            for label in self.encoded_dict:
                if label == data_point:
                    self.encoded_dict[label].append(1)
                else:
                    self.encoded_dict[label].append(0)
        return self.encoded_dict

    def show(self):
        print(self.encoded_dict)

    def to_df(self):
        import pandas as pd
        df = pd.DataFrame(self.encoded_dict)
        return df


if __name__ == '__main__':

    data = ['red','blue','green','blue']
    oh = OneHotEncoder(data)
    series = oh.fit_transform()
    oh.show()
