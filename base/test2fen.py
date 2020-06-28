import bisect

a = [6, 6]

idx = bisect.bisect_right(a, 6, 0, 1)

print(idx)
