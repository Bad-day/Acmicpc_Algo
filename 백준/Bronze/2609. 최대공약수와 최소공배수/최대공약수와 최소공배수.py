a,b = map(int,input().split())
def GCD(a,b):
        for i in range(min(a,b),0,-1):
                if a % i ==0 and b % i ==0:
                        return i
def LCM(a,b):
    for i in range(max(a,b),(a*b)+1):
        if i % a ==0 and i % b ==0:
            return i
    return a*b
q=GCD(a,b)
w=LCM(a,b)
print(f"{q}\n{w}")
