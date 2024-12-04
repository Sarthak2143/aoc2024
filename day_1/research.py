# getting all the elements and adding into left and right vector
with open('input.txt') as f:
    data = f.readlines()

left = []
right = []

for d in data:
    left.append(int(d.split("   ")[0]))
    right.append(int(d.split("   ")[1]))

left.sort()
right.sort()

def part_1():
    sum_d = 0
    for i in range(len(left)):
        d = abs(left[i] - right[i])
        sum_d += d

    print(sum_d)

def kronecker_delta(x, y):
    if x == y: return 1
    return 0

def part_2():
    sum_multiples = 0
    for i in range(len(left)):
        sum_delta = 0
        for j in range(len(right)):
            sum_delta += kronecker_delta(left[i], right[j])
        sum_multiples += left[i]*sum_delta
    
    print(sum_multiples)

part_1()
part_2()