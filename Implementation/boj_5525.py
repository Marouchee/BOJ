import sys
input = sys.stdin.readline

n=int(input())
m=int(input())

s=list(input().rstrip())
count=0

i=0
t_count=0
while i < m-2:
  if s[i]=='I' and s[i+1]=='O' and s[i+2]=='I':
    i+=2
    t_count+=1
    if t_count==n:
      count+=1
      t_count-=1
  else:
    i+=1
    t_count=0

print(count)