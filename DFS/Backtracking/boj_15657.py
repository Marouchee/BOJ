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
    
  for i in a:
    if not s:
      s.append(i)
      dfs()
      s.pop()
    elif i>=s[-1]:
      s.append(i)
      dfs()
      s.pop()

dfs()
