# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.go = 0
        self.array = None

    def go_a_step(self, i, j):
        if  i < 0 or j < 0 or i >= len(self.array) or j >= len(self.array[0]):
            return
        elif self.array[i][j] == 0:
            return
        else:
            num1 = [int(m) for m in str(i)]
            num2 = [int(m) for m in str(j)]
            sum12 = sum(num1) + sum(num2)
            if sum12 <= self.threshold:
                self.array[i][j] = 0
                self.go+=1
                self.go_a_step(i + 1, j)
                self.go_a_step(i - 1, j)
                self.go_a_step(i, j + 1)
                self.go_a_step(i, j - 1)
            else:
                self.array[i][j] = 0
                return


    def movingCount(self, threshold, rows, cols):
        self.array = [[1 for i in range(cols)] for j in range(rows)]
        self.threshold = threshold
        # write code here
        self.go_a_step(0,0)
        return self.go
Solution().movingCount(10,1,100)