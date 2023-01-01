import sys
input = sys.stdin.readline
# 팩토리얼 0구하기 -> 5 , 25, 125 
def b_1676():
    N = int(input())
    if N<25:
        print(N//5)
    elif N<125:
        print(N//5+N//25)
    else:
        print(N//5+N//25+N//125)

b_1676()

