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


n, m = map(int, input().split())

parent = [0]*n
for i in range(n):
    parent[i] = i

ans = 0

for i in range(1, m+1):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        ans = i
        break
    else:
        union_parent(parent, a, b)

print(ans)
