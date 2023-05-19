import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
broken=list(map(int, input().split()))

minV=abs(100-n)

for i in range(1000001):
  t_n=str(i)
  for j in range(len(t_n)):
    if int(t_n[j]) in broken:
      break

    elif j==len(t_n)-1:
      minV=min(minV, abs(i-n)+len(t_n))

print(minV)