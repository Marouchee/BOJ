import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph=[]

for _ in range(n):
  graph.append(list(map(int, input().split())))

dp=[]

for _ in range(n+1):
  dp.append([0]*(n+1))

for i in range(1,n+1):
  for j in range(1,n+1):
    dp[i][j] = dp[i][j-1] + graph[i-1][j-1]

for _ in range(m):
  temp=0
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(x1, x2+1):
    temp = temp + dp[i][y2] - dp[i][y1-1]
  print(temp)
