with open("input.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = [int(j) for j in data[i].split(" ")]

safe = 0
for row in data:
    status = False
    if row == sorted(row) or row == sorted(row, reverse=True):
        for i in range(len(row)-1):
            if abs(row[i] - row[i+1]) in range(1,4):
                status = True
            else:
                status = False
                break
    if status == True: safe += 1

print(safe)