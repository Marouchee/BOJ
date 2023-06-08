from collections import deque
import sys
input = sys.stdin.readline

n,m=map(int , input().split())

visited=[[False for _ in range(m)] for _ in range(n)]
graph=[]
distance=[[-1 for _ in range(m)] for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

q=deque()

for _ in range(n):
  graph.append(list(map(int, input().split())))

for i in range(n):
  for j in range(m):
    if graph[i][j]==2:
      q.append((i,j,0))
      distance[i][j]=0
      visited[i][j]=True

    elif graph[i][j]==0:
      distance[i][j]=0

while q:
  x,y,d=q.popleft()

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx>=n or ny>=m or nx<0 or ny<0:
      continue
    
    if visited[nx][ny] or graph[nx][ny]==0:
      continue

    q.append((nx, ny, d+1))
    visited[nx][ny]=True
    distance[nx][ny]=d+1

for i in range(n):
  for j in range(m):
    print(distance[i][j], end=' ')
  print()
