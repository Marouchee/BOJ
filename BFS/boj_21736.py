from collections import deque
import sys
input = sys.stdin.readline

n,m=map(int , input().split())

visited=[[False for _ in range(m)] for _ in range(n)]
campus=[]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

q=deque()
meet=0

for _ in range(n):
  campus.append(list(input().rstrip()))

for i in range(n):
  for j in range(m):
    if campus[i][j]=='I':
      q.append((i,j))
      visited[i][j]==True

while q:
  x,y=q.popleft()

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx>=n or ny>=m or nx<0 or ny<0:
      continue
    if visited[nx][ny]==True or campus[nx][ny]=='X':
      continue
    if campus[nx][ny]=='P':
      meet+=1
    q.append((nx,ny))
    visited[nx][ny]=True

if meet!=0:
  print(meet)
else:
  print('TT')
