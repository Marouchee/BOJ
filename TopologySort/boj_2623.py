from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
result = []

for _ in range(m):
    t_list = list(map(int, input().split()))
    for i in range(1, t_list[0]+1):
        for j in range(i+1, t_list[0]+1):
            graph[t_list[i]].append(t_list[j])
            indegree[t_list[j]] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(result) != n:
    print(0)
else:
    for i in result:
        print(i)
