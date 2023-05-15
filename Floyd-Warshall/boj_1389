import sys
input = sys.stdin.readline

n,m=map(int,input().split())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
  graph[i][i]=0
  graph[i][0]=0

for _ in range(m):
  a,b=map(int, input().split())
  graph[a][b]=1
  graph[b][a]=1

for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      graph[j][k]=min(graph[j][k], graph[j][i]+graph[i][k])


min_value=INF
min_index=INF

for i in range(1,n+1):
  if min_value>sum(graph[i]):
      min_value=sum(graph[i])
      min_index=i

print(min_index)
