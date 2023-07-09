import sys
input = sys.stdin.readline

n = int(input())
graph = []
ans = int(1e9)

for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(3):
    dp = [[int(1e9)]*3 for _ in range(n)]

    dp[0][k] = graph[0][k]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + graph[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + graph[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + graph[i][2]

    for i in range(3):
        if k != i:
            ans = min(ans, dp[-1][i])

print(ans)
