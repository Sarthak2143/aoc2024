with open('input.txt') as f:
    data = f.read()

def kronecker_delta(a,b):
    if a == b: return 1
    return 0

def check_string(string):
    status = True
    # check string for any illegal context, should only include ), ",", range(0,10)
    for s in string:
        if not s in [")", ","] and not s.isdigit():
            status = False

    # check for only 1 ) and 1 ","
    sum_bracket = 0
    sum_comma = 0
    for s in string:
        sum_bracket += kronecker_delta(")", s)
        sum_comma += kronecker_delta(",", s)
    if sum_bracket != 1 or sum_comma != 1: return False
    return status

db = []
for i in range(len(data)-3):
    if data[i:i+4] == "mul(" and data[i+4].isdigit():
        for x in range(8, 13):
            text = data[i:i+x]
            if check_string(data[i+4:i+x]):
                db.append(text)

sum = 0
for d in db:
    try:
        num_1 = int(d.split(",")[0][4:])
        num_2 = int(d.split(",")[-1][:-1])
        sum += num_1*num_2
    except ValueError:
        print(d)

print(sum)