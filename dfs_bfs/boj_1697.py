from collections import deque
import sys
input = sys.stdin.readline

graph=[0 for _ in range(100001)]

n,k=map(int,input().split())

def bfs(n,k):
  q = deque()
  q.append(n)
  
  while q:
    x=q.popleft()
    if x==k:
      break

    for nx in (x-1, x+1, x*2):
      if 0<=nx<=100000 and not graph[nx]:
        graph[nx]=graph[x]+1
        q.append(nx)


bfs(n,k)

print(graph[k])