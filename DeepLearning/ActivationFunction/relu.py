
def relu(number:float)->int:

    return 1 if number>0 else 0

data = [1,2,4,0,-2,4,-2,5]

output = []
for i in data:
    output.append(relu(i))


print(f"Input : {data} \n")
print("Relu Output : \n")
print(output)
