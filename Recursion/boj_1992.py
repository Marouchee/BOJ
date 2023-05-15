import sys
input = sys.stdin.readline

n=int(input())

video=[[] for _ in range(n)]

for i in range(n):
  video[i]=list(input().rstrip())

def rec(x,y,n):
  f_value=video[x][y]

  for i in range(x,x+n):
    for j in range(y,y+n):
      if f_value != video[i][j]:
        print('(',end='')
        for k in range(2):
          rec(x+(n//2)*k,y,n//2)
          rec(x+(n//2)*k,y+n//2,n//2)
        print(')',end='')
        return

  if f_value == '1':
    print(1,end='')
  else:
    print(0,end='')

rec(0,0,n)