import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

ans = 0
if n == 1:
    print(0)
else:
    for _ in range(n-1):
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        ans += a + b
        heapq.heappush(arr, a + b)
    print(ans)
