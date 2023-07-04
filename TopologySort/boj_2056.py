from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time = [0]*(n+1)
dp = [0]*(n+1)

for i in range(1, n+1):
    t_list = list(map(int, input().split()))
    time[i] = t_list[0]
    for j in range(2, 2 + t_list[1]):
        graph[t_list[j]].append(i)
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
        dp[i] = max(dp[i], time[i] + dp[now])
        if indegree[i] == 0:
            q.append(i)

print(max(dp))
