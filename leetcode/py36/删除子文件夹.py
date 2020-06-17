class Solution:
    def removeSubfolders(self, folder):
        res, t = [], '//'
        for f in sorted(folder):
            if not f.startswith(t):
                res.append(f)
                t = f + '/'
        return res


folder = ["/a", "/a/b/c", "/a/b/d", "/b", "/b/v"]
print(Solution().removeSubfolders(folder))
