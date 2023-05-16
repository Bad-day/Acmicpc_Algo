# import sys; input=sys.stdin.readline()
n = int(input()); start=666
# 1. 스타트 666, '666' 키워드가 있는 모든 요소들을 배열로 만들어서 순서 입력하면 바로 출력하게
while True:
    if '666' in str(start):
        n -=1
        if n==0:
            break
    start +=1
print(start)