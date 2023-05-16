from collections import deque
import sys
input = sys.stdin.readline

t=int(input())

for _ in range(t):
  ei=0
  p=list(input().rstrip())
  n=int(input())
  nums=input().rstrip()[1:-1].split(',')
  q=deque(nums)
  rev=0

  if n==0:
    q=[]
  
  for i in range(len(p)):
    if p[i]=='R':
      rev+=1
    else:
      if not q:
        print('error')
        ei=1
        break
      if rev%2==0:
        q.popleft()
      else:
        q.pop()
  if ei==0:
    if rev%2==0:
      print('['+','.join(q)+']')
    else:
      q.reverse()
      print('['+','.join(q)+']')
