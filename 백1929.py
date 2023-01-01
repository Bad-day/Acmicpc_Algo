#원래 알고리즘 생각 -> 1제외 모든 숫자를 리스트에 다 담은 후
# 에라토테네스 적용 %2 %3 %5 %7한 리스트 요소 for문으로 출력 but, 시간초과
# 해결방법 -> 소수인지 검사할때 2부터 i까지 검사하는것이 아닌 2부터 i의 제곱근 까지만 검사
# 에라토스테네스 -> 오래걸림 / 제곱근으로 판정 -> 효율적 
import sys
input = sys.stdin.readline
def check_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1): #num^1/2 +1 
            if num%i == 0:
                return False
        return True
m,n = map(int, input().split())
for i in range(m,n+1): # 5 부터 10까지
    if check_prime(i):
        print(i)
    
