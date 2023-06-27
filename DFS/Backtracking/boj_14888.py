import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dx = list(map(int, input().split()))
max_v = -1e9
min_v = 1e9

def dfs(k, ans):
  global max_v, min_v, dx
  
  if k == n:
    max_v = max(ans, max_v)
    min_v = min(ans, min_v)
    return

  if dx[0]>0:
    dx[0]-=1
    dfs(k+1, ans + a[k])
    dx[0]+=1

  if dx[1]>0:
    dx[1]-=1
    dfs(k+1, ans - a[k])
    dx[1]+=1

  if dx[2]>0:
    dx[2]-=1
    dfs(k+1, ans * a[k])
    dx[2]+=1

  if dx[3]>0:
    dx[3]-=1
    dfs(k+1, int(ans / a[k]))
    dx[3]+=1

dfs(1,a[0])

print(max_v)
print(min_v)
