class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            start = 0
            end = 1
            now_word = set()
            now_word.add(s[0])
            res = 1
            while start <= end and end < n:
                while end < n and s[end] not in now_word:
                    now_word.add(s[end])
                    end += 1
                    res = max(res, end - start)
                now_word.remove(s[start])
                start += 1
            return res

ans = Solution().lengthOfLongestSubstring("bbbbbfgk")
print(ans)