def twofen_idx(a, left, right, num):
    while left < right:
        mid = (left + right) // 2
        if num > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left


def twofen_insert_sort(a, n):
    for i in range(1, n):
        if a[i - 1] > a[i]:
            j = twofen_idx(a, 0, i - 1, a[i])
            shaobing = a[i]
            for k in range(i - 1, j - 1, -1):
                a[k + 1] = a[k]
            a[j] = shaobing


a = [1, 3, 2, 4, 5]
twofen_insert_sort(a, 5)
print(a)
