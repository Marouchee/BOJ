from collections import deque
import sys
input = sys.stdin.readline

t=int(input())

for _ in range(t):
  first, target= map(int, input().split())
  visited=[False]*100001
  
  q=deque()
  q.append((first,''))
  visited[first]=True
  
  while q:

    num, s = q.popleft()
    visited[num]=True
    
    if num==target:
      print(s)
      break

        #1
    t_num=(num*2)%10000
      
    if not visited[t_num]:
      q.append((t_num, s+'D'))
      visited[t_num]=True

        #2
    t_num=(num-1)%10000
        
    if not visited[t_num]:
      q.append((t_num, s+'S'))
      visited[t_num]=True


        #3
    t_num = ((10*num)+num//1000)%10000

    if not visited[t_num]:
      q.append((t_num, s+'L'))
      visited[t_num]=True

        #4
    t_num = ((num//10)+(num%10)*1000)%10000

    if not visited[t_num]:
      q.append((t_num, s+'R'))
      visited[t_num]=True
