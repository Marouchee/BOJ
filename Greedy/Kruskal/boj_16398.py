import sys
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


n = int(input())
parent = [0]*(n)
result = 0

for i in range(n):
    parent[i] = i

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

edges = []

for i in range(n):
    for j in range(i+1, n):
        edges.append((matrix[i][j], i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
