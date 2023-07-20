import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a in electro and b in electro:
        return False
    elif a in electro:
        parent[b] = a
        return True
    elif b in electro:
        parent[a] = b
        return True
    elif a < b:
        parent[b] = a
        return True
    else:
        parent[a] = b
        return True


n, m, k = map(int, input().split())
electro = list(map(int, input().split()))

parent = [0]*(n+1)
edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        if union_parent(parent, a, b):
            result += cost

print(result)
