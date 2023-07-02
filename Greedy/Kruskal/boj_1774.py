import sys
import math
input = sys.stdin.readline


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [0]*(n+1)
result = 0.00

for i in range(n+1):
    parent[i] = i

index = [(0, 0)]
for _ in range(n):
    x, y = map(int, input().split())
    index.append((x, y))

edges = [(0, 0, 0)]
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cost = math.sqrt(((index[i][0] - index[j][0])**2) + ((index[i][1] - index[j][1])**2))
        edges.append((cost, i, j))

edges.sort()

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a, b)
        result += cost

print('%.2f' %(result))
