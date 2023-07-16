from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
board = []

for _ in range(n):
    board.append(list(input().rstrip()))


q = deque()
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
visited = set()
find_ans = 0

R = [0, 0]
B = [0, 0]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            B = [i, j]
        if board[i][j] == 'R':
            R = [i, j]

q.append((R[0], R[1], B[0], B[1], 0))
visited.add((R[0], R[1], B[0], B[1]))

while q:
    rx, ry, bx, by, time = q.popleft()

    if board[rx][ry] == 'O':
        print(time)
        find_ans = 1
        break

    if time >= 10:
        continue

    for i in range(4):
        nrx = rx + dx[i]
        nry = ry + dy[i]
        nbx = bx + dx[i]
        nby = by + dy[i]
        r_move = 0
        b_move = 0

        while True: # 빨강구슬 이동
            if board[nrx][nry] == '#':
                nrx -= dx[i]
                nry -= dy[i]
                break
            elif board[nrx][nry] == 'O':
                break

            nrx += dx[i]
            nry += dy[i]
            r_move += 1

        while True: # 파랑구슬 이동
            if board[nbx][nby] == '#':
                nbx -= dx[i]
                nby -= dy[i]
                break
            elif board[nbx][nby] == 'O':
                break

            nbx += dx[i]
            nby += dy[i]
            b_move += 1

        if board[nbx][nby] == 'O':
            continue

        if nrx == nbx and nry == nby:
            if r_move > b_move:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]

        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, time+1))

if find_ans == 0:
    print(-1)
