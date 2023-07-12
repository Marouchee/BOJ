from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
graph = []
ans = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))


def move(board, way):
    if way == 0: #동
        for i in range(n):
            top = n-1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = temp
                    elif board[i][top] == temp:
                        board[i][top] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = temp

    if way == 1: #서
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = temp
                    elif board[i][top] == temp:
                        board[i][top] = temp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = temp

    if way == 2: #남
        for j in range(n):
            top = n-1
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = temp
                    elif board[top][j] == temp:
                        board[top][j] = temp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = temp

    if way == 3: #북
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = temp
                    elif board[top][j] == temp:
                        board[top][j] = temp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = temp

    return board


def dfs(board, k):
    global ans
    if k == 5:
        for i in range(n):
            for j in range(n):
                ans = max(board[i][j], ans)
        return

    for i in range(4):
        temp_board = move(deepcopy(board), i)
        dfs(temp_board, k+1)


dfs(graph, 0)
print(ans)
