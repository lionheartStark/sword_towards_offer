from collections import Counter
import math
P = 10**9+7

def C(m, n):
    p = P

    def power(x, y):  # 求x的y次方
        p = P
        res = 1
        while y:
            if y % 2 != 0:
                res *= (x % p)
            y >>= 1
            x *= (x % p)
        return res

    a = (math.factorial(n)) % p
    b = (power(math.factorial(m), (p - 2))) % p
    c = (power(math.factorial(n - m), (p - 2))) % p
    return (a * b * c % p)


def get_kind_num(deep_list):
    num_count = Counter(deep_list)
    print(num_count)
    deep = 1
    ans = 1

    while True:
        this_layer_position = num_count[deep - 1] * 2
        if deep not in num_count:
            break
        this_layer_node = num_count[deep]
        ans *= C(this_layer_node, this_layer_position)%P
        deep += 1
    print(ans%P)


get_kind_num([1, 0, 2, 2])
