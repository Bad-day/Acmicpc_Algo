import sys; k=sys.stdin.readline
#n_A = 집합 a의 원소의 개수 / n_B = 집합 b의 원소의 개수 , A ,B는 각각 요소
n_A, n_B= map(int, k().split())
A = list(map(int, input().split()));B = list(map(int, input().split()))
A, B = set(A), set(B)
if len(A-B) == 0:
    print(0)
else:
    print(len(A-B));R=sorted(A-B)
    for i in R:
        print(i,end=' ')
        
  
#숏코      
# input()
# r=set(map(int,input().split()))-set(map(int,input().split()))
# print(len(r))
# print(*sorted(r))