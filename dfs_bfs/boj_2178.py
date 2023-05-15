from collections import deque
import sys
input = sys.stdin.readline

n,m=map(int, input().split())

graph=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

def bfs(x,y):
  q=deque()
  q.append((x,y))

  while q:
    a,b=q.popleft()
    for i in range(4):
      if a+dx[i]<0 or a+dx[i]>=n or b+dy[i]<0 or b+dy[i]>=m:
        continue
      if graph[a+dx[i]][b+dy[i]]==1:
        graph[a+dx[i]][b+dy[i]] = graph[a][b] + 1
        q.append((a+dx[i], b+dy[i]))

  return graph[n-1][m-1]

print(bfs(0,0))