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