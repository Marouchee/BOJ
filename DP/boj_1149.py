import sys
input = sys.stdin.readline

n = int(input())

h=[[] for _ in range(n)]
dp=[[] for _ in range(n)]
for i in range(n):
  h[i]=list(map(int, input().split()))

dp[0].append(h[0][0])
dp[0].append(h[0][1])
dp[0].append(h[0][2])

for i in range(1,n):
  dp[i].append(min(dp[i-1][1], dp[i-1][2])+h[i][0])
  dp[i].append(min(dp[i-1][0], dp[i-1][2])+h[i][1])
  dp[i].append(min(dp[i-1][0], dp[i-1][1])+h[i][2])

print(min(dp[n-1]))
