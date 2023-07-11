import math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())

    graph = []
    n = int(input())
    ans = 0

    for _ in range(n):
        a, b, r = map(int, input().split())
        graph.append((a, b, r))

    for i in graph:
        dist1 = math.sqrt((x1-i[0])**2 + (y1-i[1])**2)
        dist2 = math.sqrt((x2-i[0])**2 + (y2-i[1])**2)
        if i[2] > dist1 and i[2] > dist2:
            continue
        elif i[2] > dist1:
            ans += 1
        elif i[2] > dist2:
            ans += 1

    print(ans)
