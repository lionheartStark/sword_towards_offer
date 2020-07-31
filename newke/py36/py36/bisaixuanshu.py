


from collections import Counter

def make_who_win(nums):

    map = Counter(nums)

    maplist = list((map.items()))

    maplist.sort()

    print(maplist)

    start = len(maplist)-1

    if maplist[start][1] & 1:
        print("1 win")
        return
    else:
        while start >= 0:
            # 奇数
            if maplist[start][1] & 1:
                print("1 win")
                return
            start -= 1
    print("2 win")

make_who_win([1,1,1,2,2,2,2])

