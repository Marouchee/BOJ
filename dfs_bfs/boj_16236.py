from collections import deque
import sys
input = sys.stdin.readline

n=int(input())

graph=[[] for _ in range(n)]
visited=[[0]*n for _ in range(n)]

for i in range(n):
  graph[i]=list(map(int, input().split()))

q=deque()
size=2
ate=0
move=0
dx=[-1,0,0,1]
dy=[0,-1,1,0]

for i in range(n):
  for j in range(n):
    if graph[i][j]==9:
      q.append((i,j))
      graph[i][j]=0
      visited[i][j]=1
      break


while 1:
  can_eat=[]
  
  while q:
    x,y = q.popleft()
    
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=n:
        continue
      if visited[nx][ny]:
        continue
        
      if graph[nx][ny]>size:
        continue
        
      elif graph[nx][ny]==size or graph[nx][ny]==0:
        q.append((nx,ny))
        visited[nx][ny]= visited[x][y] + 1
        
      elif graph[nx][ny]<size and graph[nx][ny]!=0:       
        visited[nx][ny]= visited[x][y]+1
        can_eat.append((visited[nx][ny]-1, nx, ny))

  if not can_eat:
    break

  can_eat.sort(key=lambda x: (x[0], x[1], x[2]))

  t_move, t_x, t_y = can_eat[0]
  
  move+=t_move
  ate+=1
  if size==ate:
    size+=1
    ate=0

  q.append((t_x, t_y))
  graph[t_x][t_y]=0
  
  visited=[[0]*n for _ in range(n)]
  visited[t_x][t_y]=1


print(move)