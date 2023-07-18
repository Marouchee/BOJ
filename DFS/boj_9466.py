import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False]*n
    ans = []

    def dfs(k, v_arr):
        global ans
        v_arr.append(k)
        visited[k] = True

        if visited[arr[k]]:
            if arr[k] in v_arr:
                ans += v_arr[v_arr.index(arr[k]):]
                return
        else:
            dfs(arr[k], v_arr)


    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, [])

    print(n - len(ans))
