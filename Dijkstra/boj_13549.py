import heapq
import sys
input = sys.stdin.readline
INF=int(1e9)

n,k=map(int, input().split())

distance=[INF]*(100001)

def dijkstra(start, end):
  q=[]
  heapq.heappush(q, (0, start))
  distance[start]=0

  while q:
    dist, now = heapq.heappop(q)
    
    if dist > distance[now]:
      continue

    for i in (now-1, now+1):
      if i>=0 and i<=100000:
        cost = dist + 1
        if cost < distance[i]:
          distance[i] = cost
          heapq.heappush(q, (cost, i))
    if now*2 <= 100000:
      if dist < distance[now*2]:
        distance[now*2] = dist
        heapq.heappush(q, (dist, now*2))

dijkstra(n,k)
print(distance[k])
