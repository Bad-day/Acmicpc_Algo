n = int(input());result=0
sc = list(map(int, input().split()))
k=max(sc)*100
for i in range(n):
    result += sc[i]/k
av = result / n * 100
print(av*100)
    