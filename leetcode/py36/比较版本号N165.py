class Solution:
    """
    比较两个版本号 version1 和 version2。
    如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

    你可以假设版本字符串非空，并且只包含数字和 . 字符。

     . 字符不代表小数点，而是用于分隔数字序列。

    例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

    你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
    """
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        n1 = len(version1)
        n2 = len(version2)
        if n1 < n2:
            t = [0 for i in range(n2 - n1)]
            version1.extend(t)
        elif n1 > n2:
            t = [0 for i in range(-n2 + n1)]
            version2.extend(t)

        for i in range(len(version1)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1

        return 0

ans = Solution().compareVersion( version1 = "0.1", version2 = "1.1")

print(ans)