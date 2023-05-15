import sys
input = sys.stdin.readline
n=int(input())

ans=[0,1,2,3,5]

i=4
while(i<n):
  ans.append(ans[i]+ans[i-1])
  i+=1

print(ans[n]%10007)
