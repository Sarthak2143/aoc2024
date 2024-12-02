with open("input.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = [int(j) for j in data[i].split(" ")]

for row in data: