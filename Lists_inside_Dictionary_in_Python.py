# File: Lists_inside_Dictionary_in_Python.py
# Description: Calculating the scores of sports team by using Lists inside Dictionary
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
# Reference to:
# [1] Valentyn N Sichkar. Lists inside Dictionary in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Lists_inside_Dictionary_in_Python (date of access: XX.XX.XXXX)


# Implementing the task
# Lists inside dictionary
# Calculating the scores of sports team
n = int(input())  # number of games
string = ''
d = {}

# Format of input is following: 
# Team;score;Team;score
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
# Format of output is following:
# Team: number_of_games number_of_wins number_of_draw_games number_of_lost_games score_of_win_games
for x, y in d.items():
    print(x, end=':')
    for z in y:
        print(z, end=' ')
    print()
