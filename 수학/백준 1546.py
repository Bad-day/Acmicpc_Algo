import sys;input=sys.stdin.readline;n=int(input())
for i in range(n):
    sum = list(map(int, input().split()));max_sum=max(sum);sum.remove(max_sum)
    print(max(sum)/max_sum*100)