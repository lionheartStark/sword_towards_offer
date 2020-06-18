
def find_idx(num, sorted_list):
    if sorted_list:
        print(len(sorted_list)//2, "-------")
        if num < sorted_list[len(sorted_list)//2]:
            return 0+find_idx(num, sorted_list[:len(sorted_list)//2])
        elif num >= sorted_list[len(sorted_list)//2]:
            return len(sorted_list)//2+1+find_idx(num, sorted_list[len(sorted_list)//2+1:])
    else:
        return 0


def mysort(a_list):
    sorted_list = []
    for i in range(0, len(a_list)):
        num = a_list[i]
        idx = find_idx(num, sorted_list)
        sorted_list.insert(idx, num)
    return sorted_list


a_list = [51,34,1,2,4,2]
print(mysort(a_list))