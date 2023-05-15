import sys
input = sys.stdin.readline

n=int(input())
a1=0
a2=0
a3=0
p=[[] for _ in range(n)]

for i in range(n):
  p[i]=list(map(int, input().split()))
  
def rec(x,y,n):
  global a1, a2, a3

  f_num=p[x][y]
  for i in range(x,x+n):
    for j in range(y, y+n):
      if f_num!=p[i][j]:
        for k in range(3):
          rec(x+(n//3)*k,y,n//3)
          rec(x+(n//3)*k,y+(n//3),n//3)
          rec(x+(n//3)*k,y+(n//3)*2,n//3)
        return
  if f_num==-1:
    a1+=1
  elif f_num==0:
    a2+=1
  else:
    a3+=1

rec(0,0,n)
print(a1)
print(a2)
print(a3)
