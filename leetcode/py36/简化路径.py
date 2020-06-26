class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        /a//b////c/d//././/..
        :param path:
        :return:
        """

        while "//" in path:
            path = path.replace("//", "/")
        # print(path)

        all_path = path.split("/")
        res = []
        for i in all_path:
            if i in ['', '.']:
                continue
            res.append(i)
            if i == "..":
                res.pop(-1)
                if len(res):
                    res.pop(-1)

        ans = '/'
        for i in res:
            ans += f'{i}/'
        if len(ans) > 1:
            return ans[:-1]
        else:
            return '/'


A = "/a/./b/../../c/"
print(Solution().simplifyPath(A))
