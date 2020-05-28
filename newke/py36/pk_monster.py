input_str = input()
i_and_moster = input_str.split(" ")
i_val = int(i_and_moster[0])
moster_num = i_and_moster[-1]
#print(i_val, moster_num)
input_str = input()
moster_list = input_str.split(" ")
#print(moster_list)
moster_list = [int(i) for i in moster_list]
moster_list.sort()
#print(moster_list)

money = 0
high_money = 0
for moster_val in range(len(moster_list)):
    if i_val >= moster_list[moster_val]:
        money += 1
        if money>high_money:
            high_money = money
    else:
        if i_val + money >= moster_list[moster_val]:
            money -= moster_list[moster_val] - i_val
            i_val = moster_list[moster_val]
            money += 1
            if money > high_money:
                high_money = money
        else:
            break

print(high_money)