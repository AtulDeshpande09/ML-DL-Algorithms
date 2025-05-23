class FrequencyEncoder:

    def __init__(self,data):
        self.data = data
        self.total = len(data)
        self.output = []

    def fit_transform(self):

