a,x = map(int ,input().split())
k = list(input().split());r=[]
for _ in k:
    if int(_)<x:
        r.append(_)
print(" ".join(str(x) for x in r))