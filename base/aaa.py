a = [36, 5, 12, 9, 21]
from functools import cmp_to_key

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print(cmp_to_key(reversed_cmp))

m = sorted([36, 5, 12, 9, 21], key=cmp_to_key(reversed_cmp))
print(m)
