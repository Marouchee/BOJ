import sys
input = sys.stdin.readline

n,r,c=map(int,input().split())
k=0
while n!=0: 
  n-=1
  if r<2**n and c<2**n: #1
    continue
  elif r>=2**n and c>=2**n: #4
    k=k+3*(2**n)*(2**n)
    r-=(2**n)
    c-=(2**n)
  elif r<2**n and c>=2**n:#2
    k=k+(2**n)*(2**n)
    c-=(2**n)
  elif r>=2**n and c<2**n:#3
    k=k+2*(2**n)*(2**n)
    r-=(2**n)
  
print(k)