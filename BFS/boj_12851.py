from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
visited=[INF]*100001
way=[0]*100001

n,k = map(int, input().split())

q=deque()
q.append((n,1))
visited[n] = 0
way[n] = 1

while q:
  x, age = q.popleft()

  if x-1 >= 0:
    if visited[x-1] > age:
      visited[x-1] = age
      way[x-1] = 1
      q.append((x-1, age+1))
    elif visited[x-1] == age:
      way[x-1]+=1
      q.append((x-1, age+1))

  if x+1 <= 100000:
    if visited[x+1] > age:
      visited[x+1] = age
      way[x+1] = 1
      q.append((x+1, age+1))
    elif visited[x+1] == age:
      way[x+1]+=1
      q.append((x+1, age+1))

  if x*2 <= 100000:
    if visited[x*2] > age:
      visited[x*2] = age
      way[x*2] = 1
      q.append((x*2, age+1))
    elif visited[x*2] == age:
      way[x*2]+=1
      q.append((x*2, age+1))

print(visited[k])
print(way[k])
