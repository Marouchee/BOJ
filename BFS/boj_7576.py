from collections import deque
import sys
input = sys.stdin.readline

m,n=map(int,input().split())
box=[]
for _ in range(n):
  box.append(list(map(int, input().split())))

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs():
  day=-1
  q=deque()
  t_q=deque()
  
  for i in range(n):
    for j in range(m):
      if box[i][j]==1:
        q.append((i,j))
        
  while q:
    t_q=q
    q=deque()
    while t_q:
      y,x=t_q.popleft()
      for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=m or ny>=n:
          continue
        if box[ny][nx]==-1:
          continue
        if box[ny][nx]==0:
          box[ny][nx]=1
          q.append((ny,nx))
    day+=1

  for i in range(n):
    for j in range(m):
      if box[i][j]==0:
        return -1
  return day

print(bfs())
