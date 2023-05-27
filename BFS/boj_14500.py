import sys
input = sys.stdin.readline

n,m= map(int, input().split())

paper = [[] for _ in range(n)]
visited=[[False]*m for _ in range(n)]

for i in range(n):
  paper[i] = list(map(int, input().split()))


dx=[0,0,1,-1]
dy=[1,-1,0,0]

max_V=0

def dfs(x,y,sum,count):
  global max_V

  if count==4:
    max_V = max(max_V, sum)
    return
  
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or ny<0 or nx>=n or ny>=m or visited[nx][ny]:
      continue
    visited[nx][ny]=True
    dfs(nx,ny,sum+paper[nx][ny],count+1)
    visited[nx][ny]=False


def cross(x,y):
  global max_V

  nx=x+1
  ny=y+0
  if not(nx<0 or ny<1 or nx>=n or ny>=m-1):
    max_V=max(max_V, paper[x][y]+paper[nx][ny]+paper[nx][ny+1]+paper[nx][ny-1])

  nx=x-1
  ny=y+0
  if not(nx<0 or ny<1 or nx>=n or ny>=m-1):
    max_V=max(max_V, paper[x][y]+paper[nx][ny]+paper[nx][ny+1]+paper[nx][ny-1])

  nx=x+0
  ny=y+1
  if not(nx<1 or ny<0 or nx>=n-1 or ny>=m):
    max_V=max(max_V, paper[x][y]+paper[nx][ny]+paper[nx+1][ny]+paper[nx-1][ny])

  nx=x+0
  ny=y-1
  if not(nx<1 or ny<0 or nx>=n-1 or ny>=m):
    max_V=max(max_V, paper[x][y]+paper[nx][ny]+paper[nx+1][ny]+paper[nx-1][ny])
    

for i in range(n):
  for j in range(m):
    visited[i][j]=True
    dfs(i,j,paper[i][j],1)
    visited[i][j]=False
    cross(i,j)

print(max_V)
