def part(a_list, start, end):
    i = start
    j = end

    while (i < j):
        while i < j and a_list[i] <= a_list[j]:
            j -= 1
        if i < j:
            tmp = a_list[i]
            a_list[i] = a_list[j]
            a_list[j] = tmp
            i += 1
        while i < j and a_list[i] <= a_list[j]:
            i += 1
        if i < j:
            tmp = a_list[i]
            a_list[i] = a_list[j]
            a_list[j] = tmp
            j -= 1
    return i


def mt(a_list, start, end):
    if start < end:
        p = part(a_list, start, end)
        mt(a_list, start, p - 1)
        mt(a_list, p + 1, end)


a_list = [5, 4, 6, 3, 28, 13]

mt(a_list, 0, len(a_list) - 1)
print(a_list)
