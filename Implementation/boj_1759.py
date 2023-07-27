from itertools import combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())
arr = list(input().split())

arr.sort()

for password in combinations(arr, l):
    count = 0
    for i in password:
        if i in v:
            count += 1

    if count >= 1 and count <= l-2:
        print(''.join(password))
