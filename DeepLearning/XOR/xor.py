# There will be total of 3 neural units
# 2 in hidden layer 
# 1 in output layer

class xor:
    
    def __init__(self):
        self.h1_weights = [1,1]
        self.h2_weights = [1,1]
        self.h1_bias = 0
        self.h2_bias = -1
        self.y_weights = [1,-2]
        self.y_bias = 0

    def relu(self,x):
        return max(x,0)
    def layer_h(self , x):
        # it has two neural units
        # let's say they produce output as a1 and a2
        a1 = 0
        a2 = 0
        for i in range(len(x)):
            a1 += x[i]*self.h1_weights[i]
            a2 += x[i]*self.h2_weights[i]
        a1 += self.h1_bias
        a2 += self.h2_bias

        ## Now Apply ReLu

        a1 = self.relu(a1)
        a2 = self.relu(a2)

        return [a1 , a2]

    def output_layer(self , x):
        y = 0
        for i in range(len(x)):
            y += x[i]*self.y_weights[i]
        y += self.y_bias

        # apply relu
        y = self.relu(y)

        return y

    def predict(self , x ):

        # here we will combine two layers

        y = self.output_layer((self.layer_h(x)))
        return y



if __name__ == '__main__':

    ptn = xor()
    X = [
            [0 ,0],
            [0,1],
            [1,0],
            [1,1]
            ]
    Y = []
    print("XOR gate using perceptron")
    for i in X:
        y = ptn.predict(i)
        Y.append(y)
        print(f"Input -> {i} and output -> {y}\n")

