from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    indegree[x] += 1

base_list = []
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        base_list.append(i)
        q.append(i)

dp = [[0]*(n+1) for _ in range(n+1)]

for i in base_list:
    dp[i][i] = 1

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i[0]] -= 1
        for j in range(1, n+1):
            dp[i[0]][j] += dp[now][j] * i[1]
        if indegree[i[0]] == 0:
            q.append(i[0])

for i in base_list:
    print(i, end=' ')
    print(dp[n][i])
