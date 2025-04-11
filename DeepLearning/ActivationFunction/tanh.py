import math

def tanh(x:float)->float:

    return (math.exp(x) - math.exp(-x) )/(math.exp(x) + math.exp(-x) )

x = [4 , 4 , 6, 4 , 7 , 5 ,9]

output = []

for i in x:
    output.append(tanh(i))

print(f"Input : {x}\n")
print(f"Output : {output}\n")
print("Tanh converts into range of (-1 ,1 )")
