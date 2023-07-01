import sys
input = sys.stdin.readline

n = int(input())
aq = list(map(int, input().split()))
aq.sort()

bot = 0
top = n-1
v = abs(aq[top] + aq[bot])

ans1 = aq[bot]
ans2 = aq[top]

while bot < top:
    t_v = aq[top] + aq[bot]

    if abs(t_v) < v:
        ans1 = aq[bot]
        ans2 = aq[top]
        v = abs(t_v)

    elif t_v > 0:
        top -= 1

    else:
        bot += 1

print(ans1, ans2)
