from collections import deque
import sys
input = sys.stdin.readline

n=int(input())
k=int(input())

graph=[[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
  a,b = map(int, input().split())
  graph[a-1][b-1]=1

way=dict()
l=int(input())
for _ in range(l):
  x,c = input().split()
  way[int(x)] = c

t=0
graph[0][0]=2
x=0
y=0
q=deque()
q.append((0,0))
dx=[0,1,0,-1]
dy=[1,0,-1,0]
i=0

while True:
  t+=1
  x+=dx[i]
  y+=dy[i]
  if x>=n or y>=n or x<0 or y<0:
    break

  if graph[x][y]==0:
    graph[x][y]=2
    q.append((x,y))
    nx,ny=q.popleft()
    graph[nx][ny]=0
  elif graph[x][y]==1:
    graph[x][y]=2
    q.append((x,y))
  else:
    break

  if t in way:
    if way[t]=='D':
      i = (i+1)%4
    elif way[t]=='L':
      i = (i-1)%4
    

print(t)
