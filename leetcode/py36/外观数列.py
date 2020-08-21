class Solution:
    def countAndSay(self, n: int) -> str:
        last_res = '1'

        for m in range(1, n):
            last_word = last_res + "@"
            this_word = ''
            last_count = 1
            for i in range(1, len(last_word)):
                if last_word[i] != last_word[i - 1]:
                    this_word = this_word + str(last_count) + str(last_word[i - 1])
                    last_count = 1
                else:
                    last_count += 1
            last_res = this_word

        return last_res


print(Solution().countAndSay(5))
