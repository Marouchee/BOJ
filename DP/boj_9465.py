import sys
input = sys.stdin.readline

t=int(input())
for _ in range(t):
  n = int(input())
  sticker=[]
  for _ in range(2):
    sticker.append(list(map(int, input().split())))

  dp=[[] for _ in range(2)]
  dp[0].append(sticker[0][0])
  dp[1].append(sticker[1][0])
  if n>1:
    dp[0].append(dp[1][0]+sticker[0][1])
    dp[1].append(dp[0][0]+sticker[1][1])

  for i in range(2,n):
    dp[0].append(max(dp[1][i-2], dp[1][i-1]) + sticker[0][i])
    dp[1].append(max(dp[0][i-2], dp[0][i-1]) + sticker[1][i])

  print(max(dp[0][n-1], dp[1][n-1]))
