def bisect_left(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def twofen_insert_sort(a, n):
    for i in range(1, n):
        if a[i - 1] > a[i]:
            j = bisect_left(a, a[i], 0, i)
            print(j)
            shaobing = a[i]
            for k in range(i - 1, j - 1, -1):
                a[k + 1] = a[k]
            a[j] = shaobing


a = [3, 2, 1, 2, 1]
twofen_insert_sort(a, 5)
print(a)
