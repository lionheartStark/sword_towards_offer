def get_ipt():
    N, V = list(map(int, input().split()))
    things = []
    for i in range(N):
        a = list(map(int, input().split()))
        a[0], a[1] = a[1], a[0]
        things.append(a)

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
                if w -one_thing[1]>=0:
                    dp[w] = max(dp[w], dp[w - one_thing[1]] + one_thing[0])
    return dp[Cap]



######## 单个处理函数 ########
def single_pkg_01(dp, Cap, cost, win):
    for w in range(Cap, cost - 1, -1):
        dp[w] = max(dp[w], dp[w - cost] + win)


def single_full(dp, Cap, cost, win):
    for w in range(cost, Cap + 1):
        dp[w] = max(dp[w], dp[w - cost] + win)


def single_muti(dp, Cap, cost, win, num):
    if cost * num >= Cap:
        single_full(dp, Cap, cost, win)
        return
    k = 1
    while k < num:
        single_pkg_01(dp, Cap, cost * k, win * k)
        num = num - k
        k *= 2
    single_pkg_01(dp, Cap, cost * num, win * num)


############################################################
# 混合背包问题
def mixed_package(N, Cap, things):
    dp = [0 for i in range(Cap + 1)]
    for one_thing in things:
        cost, win, kind = one_thing
        if kind == -1:
            single_pkg_01(dp, Cap, cost, win)
        elif kind == 0:
            single_full(dp, Cap, cost, win)
        else:
            single_muti(dp, Cap, cost, win, kind)
    return dp[-1]

# 二维费用背包
def wei2_package_01(N, V, M, things):
    dp = [[0 for i in range(M+1)] for i in range(V+1)]
    for one_thing in things:
        vcost, mcost, win = one_thing
        for v in range(V, vcost - 1, -1):
            for m in range(M, mcost - 1, -1):
                dp[v][m] = max(dp[v][m], dp[v-vcost][m - mcost] + win)
    return dp[-1][-1]
