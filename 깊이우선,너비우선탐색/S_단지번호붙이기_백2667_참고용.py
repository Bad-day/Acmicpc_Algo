# cnt - 단지수 / buildings - 단지내 개수 dic/ apt
from pydoc import apropos
import sys
def print_show(): #print
    global cnt
    for apt in aparts:
        print(apt)
    print(buildings)

def make_Buildings(i,j,cnt): 
    global n,aparts, buildings
    # 1. make note to itself
    if aparts[i][j] !=cnt:
        aparts[i][j] =cnt
        buildings[cnt] +=1 
    # see up
    if i > 0 and aparts[i-1][j] ==1:
        aparts[i-1][j] =cnt
        buildings[cnt] +=1
        make_Buildings(i-1,j,cnt) #재귀
    # see down
    if i <n-1 and aparts[i+1][j] == 1:
        aparts[i+1][j]=cnt
        buildings[cnt]+=1
        make_Buildings(i+1,j,cnt)
    # see left 
    if j > 0 and aparts[i][j-1] == 1:  # if it's 1 left
        aparts[i][j-1] = cnt
        buildings[cnt] += 1
        make_Buildings(i, j-1, cnt)  # recursion
    # see right
    if j < n - 1 and aparts[i][j+1] == 1:  # if it's 1 right
        aparts[i][j+1] = cnt
        buildings[cnt] += 1
        make_Buildings(i, j+1, cnt)  # recursion

n= int(sys.stdin.readline())
aparts = []

for i in range(n):
    apart = sys.stdin.readline().split("\n")[0]
    aparts.append([int(apart[i:i+1]) for i in range(0, len(apart),1)])

cnt = 2
buildings = {}

for i in range(n):
    for j in range(n):
        if aparts[i][j] == 1: #단지 확인 안되있을경우 
            buildings[cnt] = 0 #초기화
            make_Buildings(i,j,cnt)
            cnt +=1
            
print("cnt:",cnt-2)
values = list(buildings.values())
values.sort()

for v in values:
    print(v)
