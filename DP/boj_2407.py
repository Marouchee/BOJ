import sys
input = sys.stdin.readline

n,m=map(int, input().split())

def fact(k):
  f=[1,1]
  for i in range(2,k+1):
    f.append(f[i-1]*i)
  return f[k]

print(fact(n)//(fact(n-m)*fact(m)))