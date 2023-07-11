import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = int(1e9)
top = 0
bot = 0
sum = 0

while True:
    if sum >= s:
        ans = min(ans, top - bot)
        sum -= arr[bot]
        bot += 1
    elif top == n:
        break
    else:
        sum += arr[top]
        top += 1

if ans == int(1e9):
    print(0)
else:
    print(ans)
