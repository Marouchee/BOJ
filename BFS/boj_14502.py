from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs():
  global ans
  
  q = deque()
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  safe = 0
  t_graph = copy.deepcopy(graph)
    
  for i in range(n):
    for j in range(m):
      if t_graph[i][j] == 2:
        q.append((i, j))

  while q:
    x,y = q.popleft()

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      if t_graph[nx][ny] == 1 or t_graph[nx][ny] == 2:
        continue

      t_graph[nx][ny] = 2
      q.append((nx, ny))

  for i in range(n):
    for j in range(m):
      if t_graph[i][j] == 0:
        safe+=1

  ans = max(ans, safe)


def make_wall(count):
  if count == 3:
    bfs()
    return

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        make_wall(count+1)
        graph[i][j] = 0



n,m = map(int, input().split())

graph = []
ans = 0

for _ in range(n):
  graph.append(list(map(int, input().split())))
  
make_wall(0)
print(ans)
