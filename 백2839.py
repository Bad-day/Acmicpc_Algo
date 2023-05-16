import sys; input=sys.stdin.readline
N= int(input());count=0
while N>=0:
    if N % 5 ==0:
        count +=N//5
        print(count)
        break
    N -=3
    count+=1 #3으로 divison 한 판정
else:
    print(-1) #3 혹은 5로 안나눠질때면 -1출력
# import sys

# input = sys.stdin.readline

# # 입력값을 받아옵니다.
# x = int(input())

# # 3과 5로 나누어떨어지지 않을 경우에는 -1을 반환합니다.
# if x % 3 != 0 and x % 5 != 0:
#     print(-1)
# else:
#     # 입력값에서 3과 5의 최소공배수인 15을 뺀 후, 5로 나눈 몫을 출력합니다.
#     print(((lambda x: x // 5 if x % 5 == 0 else (x // 15) * 3 if x % 15 == 0 else -1))(x - sum(map(lambda y: x % y, [3, 5]))))
