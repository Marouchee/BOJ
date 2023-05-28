import sys
input = sys.stdin.readline

a,b,c=map(int, input().split())

def rec(C,n):
  if n==1:
    return C%c
  else:
    x=rec(C, n//2)
    if n%2==0:
      return (x*x)%c
    else:
      return (x*x*C)%c

print(rec(a,b))
