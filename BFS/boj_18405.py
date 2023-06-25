from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())

graph=[]
data=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(n):
  graph.append(list(map(int, input().split())))

s,x,y = map(int, input().split())

for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j], i, j, 0))

data.sort()

q=deque(data)

while q:
  virus, a, b, age = q.popleft()

  if age == s:
    break

  for i in range(4):
    nx = a + dx[i]
    ny = b + dy[i]

    if nx<0 or ny<0 or nx>=n or ny>=n:
      continue
    
    if graph[nx][ny] == 0:
      graph[nx][ny] = virus
      q.append((virus, nx, ny, age+1))

print(graph[x-1][y-1])
