from collections import deque
import sys
input = sys.stdin.readline

n=int(input())

graph=[]

for _ in range(n):
  graph.append(list(input().rstrip()))

visit=[[False for _ in range(n)] for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

count=0

for i in range(n):
  for j in range(n):
    if visit[i][j]==False:
      count+=1
      color=graph[i][j]
      q=deque()
      visit[i][j]=True
      q.append((i,j))
      while q:
        a,b = q.popleft()
        for k in range(4):
          x=a+dx[k]
          y=b+dy[k]
          if x>=n or x<0 or y>=n or y<0:
            continue
          if visit[x][y]==True:
            continue
          if color==graph[x][y]:
            q.append((x,y))
            visit[x][y]=True

print(count, end=' ')



visit=[[False for _ in range(n)] for _ in range(n)]
count=0

for i in range(n):
  for j in range(n):
    if visit[i][j]==False:
      count+=1
      color=graph[i][j]
      q=deque()
      visit[i][j]=True
      q.append((i,j))
      while q:
        a,b=q.popleft()
        for k in range(4):
          x=a+dx[k]
          y=b+dy[k]
          if x>=n or x<0 or y>=n or y<0:
            continue
          if visit[x][y]==True:
            continue
          if color=='R' or color == 'G':
            if graph[x][y]=='R' or graph[x][y]=='G':
              q.append((x,y))
              visit[x][y]=True
          else:
            if color==graph[x][y]:
              q.append((x,y))
              visit[x][y]=True

print(count)