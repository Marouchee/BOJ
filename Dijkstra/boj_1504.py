import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,e = map(int, input().split())

graph=[[] for _ in range(n+1)]

for _ in range(e):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))

def dijkstra(start, end):
  q = []
  distance=[INF]*(n+1)
  
  distance[start]=0
  heapq.heappush(q, (0, start))

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

v1, v2 = map(int, input().split())
num1 = dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)
num2 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)

if num1>=INF and num2>=INF:
  print(-1)
else:
  print(min(num1, num2))
