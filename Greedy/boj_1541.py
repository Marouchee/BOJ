import sys
input = sys.stdin.readline

n=input()
k=n.split('-')
a=[]
b=[]
for i in k:
  a.append(i.split('+'))

for i in a:
  sum=0
  for j in range(len(i)):
    i[j]=int(i[j])
    sum+=i[j]
  b.append(sum) 

sum1=b[0]*2
for i in b:
  sum1-=i

print(sum1)