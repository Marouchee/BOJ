from collections import deque
import sys
input = sys.stdin.readline

m,n,h=map(int, input().split())

graph=[[[] for _ in range(n)] for _ in range(h)]

for i in range(h):
  for j in range(n):
    graph[i][j]=list(map(int, input().split()))

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

q=deque()
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k]==1:
        q.append((i,j,k))

age=0
while q:
  t_q=q
  q=deque()
  age+=1
  while t_q:
    a,b,c = t_q.popleft()
    for i in range(6):
      x=a+dx[i]
      y=b+dy[i]
      z=c+dz[i]

      if x<0 or y<0 or z<0 or x>=h or y>=n or z>=m:
        continue
      if graph[x][y][z]==-1 or graph[x][y][z]==1:
        continue

      graph[x][y][z]=1
      q.append((x,y,z))


flag=1
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k]==0:
        flag=0
        break
    if flag==0:
      break
  if flag==0:
    break

if flag==1:
  print(age-1)
else:
  print(-1)