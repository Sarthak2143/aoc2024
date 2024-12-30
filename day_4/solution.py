# notes:
"""
1. iterate every row and find insatnces of x
2. how many 4 letter distance it have until it hit the wall?
3. check them and count them
"""

# opeing the file and getting the input
with open("input.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i][0:-1]

ll = []
for d in data:
    l = []
    for i in d:
        l.append(i)
    ll.append(l)

def check(a, b, c, d):
    if a + b + c + d == "XMAS": return True
    return False

nl = len(ll) # no. of lists
ne = len(ll[0]) # no. of elements

count = 0

for i in range(nl):
    for j in range(ne):
        # there must be 8 word formations
        # first we'll check if even these exist, starting from X
        if ll[i][j] == "X":
            # check for top and bottom
            if i - 3 >= 0: # top exists
                if check(ll[i][j], ll[i-1][j], ll[i-2][j], ll[i-3][j]):
                    count += 1
            if i + 3 < nl: # bottom exists
                if check(ll[i][j], ll[i+1][j], ll[i+2][j], ll[i+3][j]):
                    count += 1
            # check for left and right
            if j - 3 >= 0: # left exists
                if check(ll[i][j], ll[i][j-1], ll[i][j-2], ll[i][j-3]):
                    count += 1
            if j + 3 < ne: # right exists
                if check(ll[i][j], ll[i][j+1], ll[i][j+2], ll[i][j+3]):
                    count += 1
            # check for upper diagonals
            if j - 3 >= 0 and i - 3 >= 0: # upper left diagonal
                if check(ll[i][j], ll[i-1][j-1], ll[i-2][j-2], ll[i-3][j-3]):
                    count += 1
            if j + 3 < ne and i - 3 >= 0: # upper right diagonal
                if check(ll[i][j], ll[i-1][j+1], ll[i-2][j+2], ll[i-3][j+3]):
                    count += 1
            # check for lower diagonals
            if j - 3 >= 0 and i + 3 < nl: # lower left diagonal
                if check(ll[i][j], ll[i+1][j-1], ll[i+2][j-2], ll[i+3][j-3]):
                    count += 1
            if j + 3 < ne and i + 3 < nl: # lower right diagonal
                if check(ll[i][j], ll[i+1][j+1], ll[i+2][j+2], ll[i+3][j+3]):
                    count += 1
def part_1():
    print(count)

def part_2():
    count = 0
    for i in range(1, nl-1):  # Need room for the full X pattern
        for j in range(1, ne-1):
            # Check center position
            if ll[i][j] == "A":
                # Check all possible combinations of MAS/SAM in X pattern
                # Top-left to bottom-right diagonal
                if (
                    # MAS + MAS
                    (ll[i-1][j-1] == "M" and ll[i+1][j+1] == "S") and
                    (ll[i-1][j+1] == "M" and ll[i+1][j-1] == "S")
                ) or (
                    # SAM + SAM
                    (ll[i-1][j-1] == "S" and ll[i+1][j+1] == "M") and
                    (ll[i-1][j+1] == "S" and ll[i+1][j-1] == "M")
                ) or (
                    # MAS + SAM
                    (ll[i-1][j-1] == "M" and ll[i+1][j+1] == "S") and
                    (ll[i-1][j+1] == "S" and ll[i+1][j-1] == "M")
                ) or (
                    # SAM + MAS
                    (ll[i-1][j-1] == "S" and ll[i+1][j+1] == "M") and
                    (ll[i-1][j+1] == "M" and ll[i+1][j-1] == "S")
                ):
                    count += 1
    
    print(count)

part_2()