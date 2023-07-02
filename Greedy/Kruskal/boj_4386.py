import sys
import math
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a


n = int(input())
parent = [0]*(n+1)
result = 0.00

for i in range(1, n+1):
    parent[i] = i

index = []
edges = []
for _ in range(n):
    x, y = map(float, input().split())
    index.append((x, y))

for i in range(n):
    for j in range(i+1, n):
        cost = round(math.sqrt(((index[i][0]-index[j][0])**2) + ((index[i][1]-index[j][1])**2)), 2)
        edges.append((cost, i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
