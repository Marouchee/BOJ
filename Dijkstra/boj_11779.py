import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

start, end = map(int, input().split())

way=[0]*(n+1)
distance=[INF]*(n+1)

def dijkstra(start):
  q=[]
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        way[i[0]] = now
        heapq.heappush(q, (cost, i[0]))


dijkstra(start)

ans = []
temp = end
while temp != start:
  ans.append(str(temp))
  temp = way[temp]

ans.append(str(start))
ans.reverse()

print(distance[end])
print(len(ans))
print(' '.join(ans))
