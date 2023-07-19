import sys
input = sys.stdin.readline

graph = []
blank = []

for _ in range(9):
    graph.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))


def dfs(count):
    if count == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    x = blank[count][0]
    y = blank[count][1]

    for k in range(1, 10):
        flag = 0
        for t in range(9):
            if k == graph[x][t] or k == graph[t][y]:
                flag = 1
                break
        for i in range(3*(x//3), 3*(x//3) + 3):
            for j in range(3*(y//3), 3*(y//3) + 3):
                if graph[i][j] == k:
                    flag = 1
                    break
        if flag == 0:
            graph[x][y] = k
            dfs(count+1)
            graph[x][y] = 0


dfs(0)
