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
    if i not in s:
      s.append(i)
      dfs()
      s.pop()

dfs()
