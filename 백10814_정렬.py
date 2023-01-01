import sys; input=sys.stdin.readline
n=int(input());sample=[]
for i in range(n):
    a,b = map(str, input().split());sample.append([int(a),i,b])
sample.sort()
for j in range(n):
    print(sample[j][0], sample[j][2])