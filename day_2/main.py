with open("input.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = [int(j) for j in data[i].split(" ")]

def check_row_safety(row):
    status = False
    if row == sorted(row) or row == sorted(row, reverse=True):
        for i in range(len(row)-1):
            if abs(row[i] - row[i+1]) in range(1,4):
                status = True
            else:
                status = False
                break
    return status

def part_1():
    safe = 0
    for row in data:
        if check_row_safety(row) == True: safe += 1

    print(safe)

def part_2():
    safe = 0
    for row in data:
        if check_row_safety(row) == True: safe += 1
        else:
            for i in range(len(row)):
                new_list = row[:i] + row[i+1:]
                if check_row_safety(new_list):
                    safe += 1
                    break
    
    print(safe)

part_2()