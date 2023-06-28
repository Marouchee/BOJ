import sys
input = sys.stdin.readline

n = int(input())

x=[]
y=[]

for _ in range(n):
  a,b = map(int, input().split())
  x.append(a)
  y.append(b)

x.append(x[0])
y.append(y[0])

t_x=0
t_y=0

for i in range(n):
  t_x = t_x + (x[i]*y[i+1])
  t_y = t_y + (y[i]*x[i+1])

ans = t_x - t_y
ans = round(abs(ans/2), 1)
print(ans)
