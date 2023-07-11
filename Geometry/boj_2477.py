import sys
input = sys.stdin.readline

k = int(input())

#423131 ㄱ
#414231 ┏
#142423 ┗
#142323 ┛
way = []
num = []
ans = 0
for _ in range(6):
    a, b = map(int, input().split())
    way.append(a)
    num.append(b)

for i in range(6):
    if i == 0:
        if way[i] == way[i+2] and way[i+1] == way[i+3]:
            ans = num[4] * num[5] - num[i+2] * num[i+1]
            break
    if i == 1:
        if way[i] == way[i+2] and way[i+1] == way[i+3]:
            ans = num[5] * num[0] - num[i+2] * num[i+1]
            break
    if i == 2:
        if way[i] == way[i+2] and way[i+1] == way[i+3]:
            ans = num[0] * num[1] - num[i+2] * num[i+1]
            break
    if i == 3:
        if way[i] == way[i+2] and way[i+1] == way[0]:
            ans = num[1] * num[2] - num[i+1] * num[i+2]
            break
    if i == 4:
        if way[i] == way[0] and way[i+1] == way[1]:
            ans = num[2] * num[3] - num[0] * num[i+1]
            break
    if i == 5:
        if way[i] == way[1] and way[0] == way[2]:
            ans = num[3] * num[4] - num[1] * num[0]
            break
    
print(ans*k)
