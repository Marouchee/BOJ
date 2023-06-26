import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,d = map(int, input().split())

graph = [[] for _ in range(d+1)]
distance = [INF]*(d+1)

for i in range(d):
  graph[i].append((i+1, 1))

for _ in range(n):
  a,b,c = map(int, input().split())
  if b > d:
    continue
  graph[a].append((b,c))

def dijkstra(start):
  distance[start] = 0
  q=[]
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
      continue

    if graph[now]:
      for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
          distance[i[0]] = cost
          heapq.heappush(q, (cost, i[0]))

dijkstra(0)
print(distance[d])
