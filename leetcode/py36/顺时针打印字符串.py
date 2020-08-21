class Solution:
    def spiralOrder(self, matrix):
        res = []
        while len(matrix) and len(matrix[0]):
            if len(matrix):
                res.extend(matrix.pop(0))
            if len(matrix) and len(matrix[0]):
                for i in matrix:
                    res.append(i.pop(-1))
            if len(matrix):
                res.extend(matrix[-1][::-1])
                matrix.pop(-1)
            if len(matrix) and len(matrix[0]):
                for i in matrix[::-1]:
                    res.append(i.pop(0))

        print(res)
        return res


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

a1 = [
    [1, 2, 3],
    [4, 5, 6],

]

b = [
    [1],
    [2],
    [3]
]

c = [[1, 2, 4]]

d = []

Solution().spiralOrder(a1)
