#DP algo
#https://bmaru.tistory.com/102
#line1 -> testcase num t input  / int n <11
import sys; input=sys.stdin.readline; t=int(input());
def testcase(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return testcase(n-1)+testcase(n-2)+testcase(n-3)
for _ in range(t):
    n=int(input());print(testcase(n))
        
