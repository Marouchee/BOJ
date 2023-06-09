import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,x=map(int ,input().split())

graph=[[] for _ in range(n+1)]
student=[0]*(n+1)

for _ in range(m):
  u,v,w=map(int, input().split())
  graph[u].append((v,w))

def dijkstra(start, end):
  distance=[INF]*(n+1)

  q=[]
  heapq.heappush(q, (0, start))
  distance[start]=0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now]<dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

  return distance[end]

for i in range(1,n+1):
  if i!=x:
    student[i]=student[i]+dijkstra(i,x)+dijkstra(x,i)

print(max(student))
