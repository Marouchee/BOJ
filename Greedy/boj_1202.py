import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
js = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(js, (m, v))

for _ in range(k):
    c = int(input())
    bags.append(c)

bags.sort()
ans = 0
tmp = []

for bag in bags:
    while js and js[0][0] <= bag:
        heapq.heappush(tmp, -heapq.heappop(js)[1])
    if tmp:
        ans -= heapq.heappop(tmp)
    elif not js:
        break

print(ans)
