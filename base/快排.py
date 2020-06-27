def part(the_list, start, end):
    i = start
    j = end

    while (i < j):
        while i < j and the_list[i] <= the_list[j]:
            j -= 1
        if i < j:
            tmp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = tmp
            i += 1
        while i < j and the_list[i] <= the_list[j]:
            i += 1
        if i < j:
            tmp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = tmp
            j -= 1
    return i


def mt(the_list, start, end):
    if start < end:
        p = part(the_list, start, end)
        mt(the_list, start, p - 1)
        mt(the_list, p + 1, end)


the_list = [5, 4, 6, 3, 28, 13]

mt(the_list, 0, len(the_list) - 1)
print(the_list)
