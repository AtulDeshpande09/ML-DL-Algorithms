class ptn_and:

    def __init__(self):
        self.weight = [ 1,1 ]
        self.bias = -1


    def activation(self ,x):
        return 1 if x>0 else 0

    def predict(self , x):
        z = 0
        for i in range(len(x)):
            z += x[i]*self.weight[i]
        z += self.bias

        return self.activation(z)


if __name__ == '__main__':

    ptn = ptn_and()
    X = [
            [0 ,0],
            [0,1],
            [1,0],
            [1,1]
            ]
    Y = []
    print("AND gate using perceptron")
    for i in X:
        y = ptn.predict(i)
        Y.append(y)
        print(f"Input -> {i} and output -> {y}\n")
