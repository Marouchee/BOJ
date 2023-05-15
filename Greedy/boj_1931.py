import sys
input = sys.stdin.readline
n=int(input())
a=[]
ans=[]
for _ in range(n):
  a.append(list(map(int,input().split())))

a.sort(key = lambda x: (x[1], x[0]))

ans.append(a[0])
count=0
for i in range(1,n):
  if ans[count][1]<=a[i][0]:
    ans.append(a[i])
    count+=1

print(len(ans))
