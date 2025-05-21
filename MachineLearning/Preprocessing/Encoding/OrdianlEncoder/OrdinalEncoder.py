class OrdinalEncoder:

    def __init__(self,data:list):
        self.data = data
        self.unique_labels = list(set(data))
        self.no_labels = len(self.unique_labels)
        self.mapping = {i : self.unique_labels.index(i) for i in self.unique_labels}
        self.encoded_list = []

    def fit_transform(self):
        for data_point in self.data:
            self.encoded_list.append(self.mapping[data_point])
        return self.encoded_list


    def show(self):
        print(self.encoded_list)

    def to_df(self):
        import pandas as pd
        df = pd.DataFrame(self.encoded_list)
        return df


if __name__ == '__main__':

    data = ['red','blue','green','blue']
    oe = OrdinalEncoder(data)
    series = oe.fit_transform()
    oe.show()
