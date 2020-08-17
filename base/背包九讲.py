# 2维零一背包,求可装最大
def packge01_wei2(N, Cap, things):
    dp = [[0 for i in range(Cap + 1)] for j in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(1, Cap + 1):
            if w - things[i - 1][1] < 0:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - things[i - 1][1]] + things[i - 1][0])
    return dp[N][Cap]


# 1维零一背包,求可装最大
def packge01_wei1(N, Cap, things):
    dp = [0 for i in range(Cap + 1)]
    for i in range(1, N + 1):
        for w in range(Cap, things[i - 1][1] - 1, -1):
            dp[w] = max(dp[w], dp[w - things[i - 1][1]] + things[i - 1][0])
    return dp[Cap]


# 1维完全背包,求可装最大
def packge_full_wei1(N, Cap, things):
    dp = [0 for i in range(Cap + 1)]
    for i in range(1, N + 1):
        for w in range(things[i - 1][1], Cap + 1):
            dp[w] = max(dp[w], dp[w - things[i - 1][1]] + things[i - 1][0])
    return dp[Cap]


# 多重背包,按照二进制优化
def muti_packge(N, Cap, things):
    new_things = []
    for i in things:
        get = i[0]
        cost = i[1]
        amount = i[2]
        c = 1
        while amount - c > 0:
            amount -= c
            new_things.append([get * c, cost * c])
        new_things.append([get * amount, cost * amount])
    return packge01_wei1(len(new_things), Cap, new_things)


# 分组背包,每组互斥
def fenzu_package(fenzus, Cap):
    dp = [0 for i in range(Cap + 1)]

    for fenzu in fenzus:
        for w in range(Cap, 0, -1):
            for one_thing in fenzu:
                dp[w] = max(dp[w], dp[w - one_thing[1]] + one_thing[0])
    return dp[Cap]
