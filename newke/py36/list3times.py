input_str = input()
M_N = [int(i) for i in input_str.split(" ")]
host_M = M_N[0]
post_N = M_N[1]

#
input_str = input()
host_power = [int(i) for i in input_str.split(" ")]
host_power.sort()
#
a_dict = {}
for i in range(post_N):
    input_str = input()
    use_and_get = [int(i) for i in input_str.split(" ")]
    use = use_and_get[0]
    get = use_and_get[1]
    if len(host_power)>0 and use <= host_power[-1]:
        if use in a_dict:
            a_dict[use].append[get]
            a_dict[use].sort(reverse=True)
        else:
            a_dict[use] = [get]
# 开始决策
get_list = [i for i in a_dict]
get_list.sort(reverse=True)

all_get = 0
for power in host_power:
    max_get = 0
    max_need = None
    for need in get_list:
        if need <= power:
            if len(a_dict[need])>0 and max_get < a_dict[need][0]:
                max_get = a_dict[need][0]
                max_need = need
    if max_need:
        if len(a_dict[max_need])>1:
            a_dict[max_need] = a_dict[max_need][1:]
        else:
            a_dict[max_need] = []
        all_get += max_get
print(all_get)
