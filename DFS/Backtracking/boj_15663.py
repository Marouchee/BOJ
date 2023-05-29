import sys
input = sys.stdin.readline

n,m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()

s=[]
visited=[False]*n

def dfs():
  if len(s)==m:
      print(' '.join(map(str,s)))
      return
    
  printed=0
  for i in range(n):
    if not visited[i] and printed != a[i]:
      visited[i]=True
      s.append(a[i])
      printed=a[i]
      dfs()
      s.pop()
      visited[i]=False

dfs()
