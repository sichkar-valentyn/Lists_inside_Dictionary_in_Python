# Implementing the task
# Lists inside dictionary
# Calculating the scores of sports team
n = int(input())
string = ''
d = {}

for i in range(n):
    string = input().split(';')
    # If there is no yet teams in the dictionary
    if string[0] not in d:
        d[string[0]] = [1, 0, 0, 0, 0]
    else:
        d[string[0]][0] += 1
    if string[2] not in d:
        d[string[2]] = [1, 0, 0, 0, 0]
    else:
        d[string[2]][0] += 1
        
    # Calculating data
    if int(string[1]) > int(string[3]):  # Who wins
        d[string[0]][1] += 1
        d[string[0]][4] += 3
        d[string[2]][3] += 1
    elif int(string[1]) == int(string[3]):  # If draw
        d[string[0]][2] += 1
        d[string[2]][2] += 1
        d[string[0]][4] += 1
        d[string[2]][4] += 1
    elif int(string[1]) < int(string[3]):  # Who loses
        d[string[2]][1] += 1
        d[string[2]][4] += 3
        d[string[0]][3] += 1
        

# Showing the table with results
for x, y in d.items():
    print(x, end=':')
    for z in y:
        print(z, end=' ')
    print()

