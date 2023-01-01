# import sys; input=sys.stdin.readline()
N=int(input());K=int(input())
def era(K): #N = num / k= range
    count=0
    n=K
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
        for k in primes:
            if k<=N:
                primes.remove(k)
            else:
                count+=1
    print(count)
era(K)

    

