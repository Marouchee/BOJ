import sys
input = sys.stdin.readline

n,m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()

s=[]

def dfs():
  if len(s)==m:
      print(' '.join(map(str,s)))
      return
    
  printed=0
  for i in range(n):
    if not s and a[i] != printed:
      s.append(a[i])
      printed=a[i]
      dfs()
      s.pop()
    elif printed != a[i] and s[-1]<=a[i]:
      s.append(a[i])
      printed=a[i]
      dfs()
      s.pop()

dfs()
