from collections import deque
import sys
input = sys.stdin.readline

a,b=map(int, input().split())

q=deque()
q.append((a,1))
flag=1

while q:
  x,num=q.popleft()
  if x>b:
    continue
  elif x==b:
    flag=0
    print(num)
    break

  q.append((x*2, num+1))
  t_x=str(x)+'1'
  t_x=int(t_x)
  q.append((t_x, num+1))

if flag==1:
  print(-1)
