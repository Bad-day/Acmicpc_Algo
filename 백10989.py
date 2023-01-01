#set -> 중복제거 아니라 사용불가, list , append() -> 정렬 -> 하나씩 출력
# append -> 메모리 사용 높음. 
'''
import sys
n=int(sys.stdin.readline());k=[]
for i in range(n):
    k.append(int(sys.stdin.readline()))    
k.sort()
for j in k:
    print(j)
'''

import sys
input = sys.stdin.readline
n = int(input());k=[0]*10001
for _ in range(n):
    k[int(input())]+=1
for i in range(len(k)):
    if k[i]!=0:
        for j in range(k[i]):
            print(i)
# 각 숫자가 나올경우 해당 리스트의 숫자를 1씩 더해서 출력시 해당 하는 리스트 숫자만큼 정렬된채로 숫자 출력 

