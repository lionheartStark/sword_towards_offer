N, V = list(map(int, input().split()))
things = []

for i in range(N):
    a = list(map(int, input().split()))
    a[0], a[1] = a[1], a[0]
    get, cost, amount = a
    c = 1
    while amount - c > 0:
        amount -= c
        things.append([get * c, cost * c])
        c = c * 2
    things.append([get * amount, cost * amount])


def packge01_wei1(N, Cap, things):
    dp = [0 for i in range(Cap + 1)]
    for i in range(1, N + 1):
        for w in range(Cap, things[i - 1][1] - 1, -1):
            dp[w] = max(dp[w], dp[w - things[i - 1][1]] + things[i - 1][0])
    return dp[Cap]


def muti_packge(N, Cap, things):
    return packge01_wei1(len(things), Cap, things)


ans = muti_packge(N, V, things)
print(ans)
