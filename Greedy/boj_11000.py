import heapq
import sys
input = sys.stdin.readline

n = int(input())
table = []

for _ in range(n):
    a, b = map(int, input().split())
    table.append((a, b))

table.sort()
room = []

heapq.heappush(room, table[0][1])
for i in range(1, n):
    if room[0] <= table[i][0]:
        heapq.heappop(room)
        heapq.heappush(room, table[i][1])
    else:
        heapq.heappush(room, table[i][1])

print(len(room))
