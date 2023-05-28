from collections import deque
import sys
input = sys.stdin.readline

n=int(input())

node=[[] for _ in range(n+1)]
visited=[False]*(n+1)
p=[0]*(n+1)

for _ in range(n-1):
  a,b=map(int, input().split())
  node[a].append(b)
  node[b].append(a)

q=deque()
q.append(1)
while q:
  x=q.popleft()
  if visited[x]:
    continue
  if node[x]:
    for i in node[x]:
      if p[i]==0:
        p[i]=x
      q.append(i)
  visited[x]=True

for i in range(2,n+1):
  print(p[i])
