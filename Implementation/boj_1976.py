import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def find_parent(parent, x):
    if parent[x] != x:
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
m = int(input())

parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            union_parent(parent, j+1, i)

brr = list(map(int, input().split()))
flag = 0
for i in range(m-1):
    if find_parent(parent, brr[i]) != find_parent(parent, brr[i+1]):
        flag = 1
        break
if flag:
    print('NO')
else:
    print('YES')
