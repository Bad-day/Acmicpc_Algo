def fac(n):
    if n>1:
        return n*fac(n-1)
    else:
        return 1
    a = int(input())
    print(fac(a))

#k = int(input())
#print(lambda a,b: a if a>1

#result = 1
#for i in range(1, a+1, 1):
    #result *=i
#print(result)

r=i=1;exec('r*=i;i+=1;'*int(input()));print(r)
