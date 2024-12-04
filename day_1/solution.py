with open('input.txt') as f:
    data = f.readlines()

left = []
right = []

for d in data:
    left.append(int(d.split("   ")[0]))
    right.append(int(d.split("   ")[1]))

new_left = left.copy()
new_right = right.copy()

def part_1():
    distance = 0
    for _ in range(1000):
        d = abs(min(new_left) - min(new_right))
        distance += d
        new_left.remove(min(new_left))
        new_right.remove(min(new_right))

    print(distance)

#helper function
def get_num(num, data): # returns the num of appearance of num in data
    n = 0
    for d in data:
        if d == num:
            n += 1
    return n

def part_2():
    sim_score = 0
    for l in left:
        sim_score += l * get_num(l, right)

    print(sim_score)

part_1()
part_2()