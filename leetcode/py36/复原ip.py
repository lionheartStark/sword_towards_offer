from itertools import permutations
class Solution:

    def a_cut(self, the_str, now_ip):
        len_str = len(the_str)
        len_now_ip = len(now_ip)
        if len_now_ip > 4 :
            return
        elif len_now_ip == 4:
            if not the_str:
                res_str = ''.join(now_ip)
                res_str = res_str[0:-1]
                self.res.append(res_str)
            else:
                return
        elif (len_now_ip<4 and len_str/(4-len_now_ip)> 3):
            return
        if not len_str:
            return
        elif len_str == 1:
            self.a_cut(the_str[1:], now_ip+[the_str[0:1]+'.'])
        elif len_str == 2:
            self.a_cut(the_str[1:], now_ip+[the_str[0:1]+'.'])
            if 10 <= int(the_str[0:2]):
                self.a_cut(the_str[2:], now_ip + [the_str[0:2]+'.'])
        elif len_str >= 3:
            self.a_cut(the_str[1:], now_ip + [the_str[0:1]+'.'])
            if 10 <= int(the_str[0:2]):
                self.a_cut(the_str[2:], now_ip + [the_str[0:2]+'.'])
            if 100 <= int(the_str[0:3]) <= 255:
                self.a_cut(the_str[3:], now_ip + [the_str[0:3]+'.'])

    def restoreIpAddresses(self, s: str) -> list:
        self.res = []
        self.a_cut(s,[])
        return self.res
print(Solution().restoreIpAddresses("25525511135"))