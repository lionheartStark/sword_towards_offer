def sort_a_str(astr):
    len_str = len(astr)
    astr = list(astr)

    ans = ["@@" for i in range(len_str)]

    the_map = {}

    for i in range(ord("a"), ord("z")+1):
        str_i = chr(i)
        the_map[str_i] = []

    for i in range(len_str):
        if 'a' <= astr[i] <= 'z' or 'A' <= astr[i] <= 'Z':
            the_map[astr[i].lower()].append(astr[i])
        else:
            ans[i] = astr[i]
    idx = 0
    for k,v in the_map.items():
        while v:
            theword = v.pop(0)
            while ans[idx] != "@@":
                idx +=1
            ans[idx] = theword
    res = ""
    for i in ans:
        res += i
    print(res)
    return res
sort_a_str("QquY333fghuan")