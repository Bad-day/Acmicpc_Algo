import sys; input=sys.stdin.readline;alpha_list = [0]*4
name=str(input())
if name in "L":
    alpha_list[0]+1
if name in "O":
    alpha_list[1]+1
if name in "V":
    alpha_list[2]+1
if name in "E":
    alpha_list[3]+1
n=map(int, input())
for i in range(n):
    team_name=map(input())
    if team_name in "L":
        alpha_list[0]+1
    if team_name in "O":
        alpha_list[1]+1
    if team_name in "V":
        alpha_list[2]+1
    if team_name in "E":
        alpha_list[3]+1
