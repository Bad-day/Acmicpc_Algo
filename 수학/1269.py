#대칭차집합 
a, b= map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A^B))

