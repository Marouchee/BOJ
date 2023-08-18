import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
s = int(input())

for i in range(n):
    max_n = max(A[i: min(n, i + s + 1)])
    k = A.index(max_n)

    for j in range(k, i, -1):
        A[j], A[j-1] = A[j-1], A[j]

    s -= (k - i)
    if s <= 0:
        break

print(*A)
