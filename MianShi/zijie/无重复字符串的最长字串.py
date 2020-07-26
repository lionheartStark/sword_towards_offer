from collections import defaultdict
class Solution:
    def has_cf(self, a_list):
        if len(a_list) == len(set(a_list)):
            return False
        else:
            return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        max_len = 1
        i = 0
        j = 1
        while True:
            while not self.has_cf(s[i:j]):
                j += 1
                if j > len(s):
                    break
            # 此处刚好有重复
            print(s[i:j-1], len(s[i:j-1]))
            if len(s[i:j-1]) > max_len:
                max_len = len(s[i:j-1])
            i += 1
            # 此时结果不关心
            # print(s[i:j], len(s[i:j]))
            # if len(s[i:j]) > max_len:
            #     max_len = len(s[i:j])
            j += 1
            if j > len(s):
                break
        return max_len


a = ""
b = "aac"
c = "pwwkew"
d = "abcabcbb"
print("res", Solution().lengthOfLongestSubstring(b))