a=int(input());num=[]
for i in range(a):
    k=int(input())
    if k:
        num.append(k)
    else:
        del(num[-1])
print(sum(num))