import sys
input = sys.stdin.readline

n = int(input())

ans = 0
graph = [0]*n

def can_queen(k):
  for i in range(k):
    if graph[k] == graph[i] or abs(k-i) == abs(graph[k]-graph[i]):
      return False

  return True


def n_queen(k):
  global ans
  
  if k == n:
    ans+=1
    return

  else:
    for i in range(n):
      graph[k] = i
      if can_queen(k):
        n_queen(k+1)

n_queen(0)
print(ans)
