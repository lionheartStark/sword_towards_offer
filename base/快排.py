def part(the_list, start, end):
    i = start
    j = end

    while i < j:
        while i < j and the_list[i] <= the_list[j]:
            j -= 1
        if i < j:
            tmp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = tmp
            print(the_list)
            i += 1
        while i < j and the_list[i] <= the_list[j]:
            i += 1
        if i < j:
            tmp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = tmp
            print(the_list)
            j -= 1
    return i


def qucik_sort(the_list, start, end):
    if start < end:
        p = part(the_list, start, end)
        print(p)
        qucik_sort(the_list, start, p - 1)
        qucik_sort(the_list, p + 1, end)


A = [5, 4, 6, 3, 28, 13]
print(A)
qucik_sort(A, 0, len(A) - 1)
print(A)
