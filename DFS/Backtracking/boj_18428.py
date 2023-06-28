import sys
input = sys.stdin.readline

n = int(input())

graph=[]
ans = 'NO'
teacher = 0
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(n):
  data = list(input().strip().split(' '))
  teacher += data.count('T')
  graph.append(data)

def check(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    while 0<=nx<n and 0<=ny<n and graph[nx][ny] != 'O':
      if graph[nx][ny] == 'S':
        return True
      else:
        nx += dx[i]
        ny += dy[i]
      
  return False

def dfs(k):
  global ans
  
  if k == 3:
    count = 0
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 'T':
          if not check(i,j):
            count+=1

    if count == teacher:
      ans = 'YES'
    return

  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'X':
        graph[i][j] = 'O'
        k+=1
        dfs(k)
        k-=1
        graph[i][j] = 'X'

dfs(0)
print(ans)
