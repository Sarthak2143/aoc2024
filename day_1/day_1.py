with open('input.txt') as f:
    data = f.readlines()

left = []
right = []

for d in data:
    left.append(int(d.split("   ")[0]))
    right.append(int(d.split("   ")[1]))

#distance = 0
#for i in range(1000):
#    d = abs(min(left) - min(right))
#    distance += d
#    left.remove(min(left))
#    right.remove(min(right))
#
# print(distance)
def get_num(num, data): # returns the num of appearance of num in data
    n = 0
    for d in data:
        if d == num:
            n += 1
    return n

sim_score = 0
for l in left:
    sim_score += l * get_num(l, right)

print(sim_score)
