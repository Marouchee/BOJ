import sys
input = sys.stdin.readline

n = int(input())

tr=[[] for _ in range(n)]
dp=[[] for _ in range(n)]

for i in range(n):
  tr[i]=list(map(int, input().split()))

dp[0].append(tr[0][0])
if n>1:
  dp[1].append(tr[0][0]+tr[1][0])
  dp[1].append(tr[0][0]+tr[1][1])

for i in range(2,n):
  dp[i].append(dp[i-1][0]+tr[i][0])
  for j in range(len(tr[i])-2):
    dp[i].append(max(dp[i-1][j]+tr[i][j+1], dp[i-1][j+1]+tr[i][j+1]))
  dp[i].append(dp[i-1][-1]+tr[i][-1])

print(max(dp[n-1]))
