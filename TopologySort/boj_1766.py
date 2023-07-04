import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = []
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


t_list = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(t_list, i)


while t_list:
    now = heapq.heappop(t_list)
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(t_list, i)

for i in result:
    print(i, end=' ')
