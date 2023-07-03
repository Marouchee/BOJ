from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    last_result = list(map(int, input().split()))

    new_result = []
    indegree = [0]*(n+1)
    graph = [[False]*(n+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1, n):
            graph[last_result[i]][last_result[j]] = True
            indegree[last_result[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    only_output = True
    cycle = False

    for _ in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            only_output = False
            break

        now = q.popleft()
        new_result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print('IMPOSSIBLE')
    elif not only_output:
        print('?')
    else:
        for i in new_result:
            print(i, end=' ')
        print()
