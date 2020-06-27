def mysort(a_list):
    for i in range(0, len(a_list) - 1):
        print("------", i)
        for n in range(len(a_list) - 1 - i):
            print(n, n + 1)
            if a_list[n] > a_list[n + 1]:
                tmp = a_list[n]
                a_list[n] = a_list[n + 1]
                a_list[n + 1] = tmp
    return a_list


def mysort(a_list):
    n = len(a_list)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if a_list[j] > a_list[j + 1]:
                tmp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = tmp
    return a_list


a_list = [5, 4, 3, 2, 1]

print(mysort(a_list))
