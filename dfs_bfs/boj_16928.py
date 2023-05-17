from collections import deque
import sys
input = sys.stdin.readline

n,m=map(int, input().split())

dice=[1,2,3,4,5,6]

INF=1e9

graph=[INF for _ in range(101)]
visited=[False for _ in range(101)]

link=[0 for _ in range(101)]

for _ in range(n):
  x,y=map(int, input().split())
  link[x]=y

for _ in range(m):
  x,y=map(int, input().split())
  link[x]=y

q=deque()
q.append(1)
roll=0

while q:
  t_q=q
  q=deque()
  roll+=1
  while t_q:
    a=t_q.popleft()
    for i in dice:
      at=a+i
      if at>100:
        continue
      if visited[at]==True:
        continue
      if link[at]!=0:
        if visited[link[at]]==True:
          continue
        else:
          q.append(link[at])
          graph[link[at]]=roll
          visited[link[at]]=True
      else:
        graph[at]=roll
        q.append(at)
        visited[at]=True


print(graph[100])