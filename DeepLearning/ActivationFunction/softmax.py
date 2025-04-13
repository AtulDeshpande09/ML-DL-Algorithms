import math


def softmax(x , den ):
    num = math.exp(x)
    probability = num/den
    return probability

x = [1.3 , 5.1, 2.2 , 0.7 , 1.1]

print(f"Data --> {x} \n")
print("Applying Softmax")

den = 0
for i in x :
    den += math.exp(i)

output = []
for i in x :
    output.append(softmax(i , den))

print(f"Probability : {output}")
