# import sys; input=sys.stdin.readline;j=1
# n,k = map(int, input().split()) #n은 물품의수 k는 무게제한
# dick = [list(map(int, input().split())) for _ in range(n)]
# for i in range(len(dick)):
#     weight,value=dick[i][0],dick[i][1];current_weihts = k-weight #6, 13, 1
#     print(weight,value)
#     if current_weihts >= dick[i][0]:
#         weight+=dick[i][0]; value+=dick[i][1]
#         best_value=value
#         weight,value=0,0
#         print(best_value)
        
# 변수 rank, mid_w  생성, dick내 key를 순서대로 하나 받아와서 rank와 mid_w에 저장시킴 그다음 key를 순회해서 제한무게에 더 포함될수있는 key가 있는지 찾음. 있다면 rank와 mid_w에 각각 해당 키 벨류값을
#저장시킴. 그다음 두번째 key를 저장시켜 rank와 mid_w를 비교해서 더 크다면 갱신, 아니면 다음순서로 넘어감. 반복 후 가장 큰 mid_w를 출력시킴.


# dick = dict(input().split() for _ in range(n))  # case 1 : use dict

# Weighted = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]
# d = [[0]*(k+1)for _ in range(n+1)]


# ----------fix-----------------
# 당신이 제공한 코드는 배낭 문제의 기본 구현입니다.배낭 문제는 배낭의 용량을 초과하지 않으면서 총 값이 최대가 되도록 배낭을 아이템으로 채우는 것이 목표인 최적화 문제입니다.

# 단, 제공된 코드에는 해결해야 할 몇 가지 문제가 있습니다.

# current_wehts 변수는 코드에서 사용되지 않습니다.계산되지만 이후 작업에서는 사용되지 않습니다.

# weight 변수와 value 변수는 if 문에서 값을 재할당하고 있지만 이후의 조작에서는 사용되지 않습니다.

# best_value 변수에는 if 스테이트먼트 내의 값이 할당되어 있습니다만, 이후의 조작에서는 사용되지 않습니다.

# 배낭 문제를 해결하기 위해 동적 프로그래밍을 사용할 것을 제안합니다.

# 다음은 코드를 수정하는 방법의 예입니다.
import sys
input=sys.stdin.readline
n, k = map(int, input().split()) 
dick = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if dick[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-dick[i-1][0]] + dick[i-1][1])

print(dp[n][k])
