#https://rh-tn.tistory.com/32
import sys; input=sys.stdin.readline;n,k = map(int, input().split());result=0
def bino_coef ():
    if k==0 or n==k:
        r= 1
    else:
        r= bino_coef(n-1,k) + bino_coef(n-1,k-1)
    result = r%10007
print(bino_coef())
#bino_coef(4,2)
