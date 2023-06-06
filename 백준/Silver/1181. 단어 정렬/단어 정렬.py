w =[]
l = int(input())
for i in range(l):
    w.append(input().strip())
w_s = set(w)
w = list(w_s)
w.sort()
r = sorted(w, key=len)
for j in r:
    print(j)
    