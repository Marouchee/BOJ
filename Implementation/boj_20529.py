import sys
input = sys.stdin.readline

t=int(input())

for _ in range(t):
  n=int(input())
  a=list(map(str, input().split()))
  if n>32:
    print(0)
  else:
    ans=100000
    
    for i in range(n):
      for j in range(n):
        for k in range(n):
          temp=0
          if i==j or i==k or j==k:
            continue
          for l in range(4):
            if a[i][l] != a[j][l]: temp+=1
            if a[i][l] != a[k][l]: temp+=1
            if a[j][l] != a[k][l]: temp+=1

          ans= min(ans, temp)

    print(ans)
