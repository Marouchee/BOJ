from collections import deque
import sys
input = sys.stdin.readline

n=int(input())

graph=[]
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
q=deque()
h_num=[]

for i in range(n):
  for j in range(n):
    if graph[i][j]==1:
      q.append((i,j))
      graph[i][j]=0
      t_h_num=1
      while q:
        a,b=q.popleft()
        for k in range(4):
          nx=a+dx[k]
          ny=b+dy[k]
          if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
          if graph[nx][ny]==1:
            graph[nx][ny]=0
            q.append((nx,ny))
            t_h_num+=1
      h_num.append(t_h_num)

h_num.sort()

print(len(h_num))
for i in range(len(h_num)):
  print(h_num[i])