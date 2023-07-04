from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    indegree = [0]*(n+1)
    dp = [0]*(n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = D[i]

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + D[i])
            if indegree[i] == 0:
                q.append(i)

    print(dp[w])
