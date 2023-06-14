from collections import deque
import sys
input = sys.stdin.readline

n,m=map(int, input().split())

graph=[]
visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(n):
  graph.append(list(input().rstrip()))

q=deque()
q.append((0,0,0))
visited[0][0][0] = 1
noway=0

while q:
  x, y, flag = q.popleft()
  if x==n-1 and y==m-1:
    print(visited[x][y][flag])
    noway=1
    break
     
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx<0 or ny<0 or nx>=n or ny>=m:
      continue
      
    if graph[nx][ny] == '1':
      if flag == 0:
        visited[nx][ny][1] = visited[x][y][0] + 1
        q.append((nx, ny, 1))

    elif graph[nx][ny] == '0' and visited[nx][ny][flag] == 0:
      visited[nx][ny][flag] = visited[x][y][flag] + 1
      q.append((nx, ny, flag))


if noway == 0:
  print(-1)
