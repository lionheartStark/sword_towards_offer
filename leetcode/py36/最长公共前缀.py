class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        res = ""
        for i in strs:
            for j in range(len(i)):
                qian = i[:j+1]
                has = True
                for m in strs:
                    if len(qian)>len(m):
                        has = False
                        break
                    elif not qian in m[:j+1]:
                        has = False
                        break
                if has:
                    if len(qian)>len(res):
                        res = qian
                else:
                    return res
            return res
        return res
print(Solution().longestCommonPrefix(["flower","flow","flight"]))