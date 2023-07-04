from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time = [0]
dp = [0]*(n+1)

for i in range(1,n+1):
    t_list = list(map(int, input().split()))
    t_q = deque(t_list)
    time.append(t_q.popleft())
    while t_q:
        a = t_q.popleft()
        if a == -1:
            break
        graph[a].append(i)
        indegree[i] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[now] + time[i])
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(dp[i])
