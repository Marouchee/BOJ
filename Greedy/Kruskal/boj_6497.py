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


while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    parent = [0]*(m+1)

    edges = []
    result = 0
    expensive = 0

    for i in range(1, m+1):
        parent[i] = i

    for _ in range(n):
        a, b, cost = map(int, input().split())
        expensive += cost
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(expensive - result)

