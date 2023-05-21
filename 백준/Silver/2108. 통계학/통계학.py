import math;import sys; input= sys.stdin.readline
n= int(input());a=[];dick={}
for _ in range(n):
  a.append(int(input()))
print(round(sum(a)/len(a)))#n1
a.sort();print(a[n // 2])#n2
for i in a: #n3
  if i in dick:
    dick[i] += 1
  else:
    dick[i] = 1
sorted_dick = sorted(dick.items(), key=lambda x: (-x[1], x[0]))
if len(a) > 1 and sorted_dick[0][1] == sorted_dick[1][1]:
  print(sorted_dick[1][0])
else:
  print(sorted_dick[0][0])
print(max(a)-min(a))#n4