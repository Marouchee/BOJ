import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  visited=[False]*1_000_001
  max_q = []
  min_q = []
  
  for i in range(n):
    a, b = input().split()
    if a == 'I':
      heapq.heappush(max_q, (-int(b), i))
      heapq.heappush(min_q, (int(b), i))
      visited[i]=True
    elif b == '-1':
      while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
      if min_q:
        visited[min_q[0][1]]=False
        heapq.heappop(min_q)
    else:
      while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
      if max_q:
        visited[max_q[0][1]]=False
        heapq.heappop(max_q)
  
  while min_q and not visited[min_q[0][1]]:
    heapq.heappop(min_q)
  while max_q and not visited[max_q[0][1]]:
    heapq.heappop(max_q)

  if max_q and min_q:
    print(-max_q[0][0], min_q[0][0], end=" ")
  else:
    print('EMPTY')