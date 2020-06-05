import numpy as np

class Solution:

    def __init__(self):
        self.listOneCircle = []

    def oneCircle(self, matrix, s, l, c):
        if l == 1:
            for i in range(s, s + c):
                self.listOneCircle.append(matrix[s][i])
        elif c == 1:
            for j in range(s, s + l):
                self.listOneCircle.append(matrix[j][s])
        else:
            for i in range(s, s + c):
                self.listOneCircle.append(matrix[s][i])
            for j in range(s + 1 , s + l):
                self.listOneCircle.append(matrix[j][s + c - 1])
            for i in range(s + c - 2, s - 1, -1):
                self.listOneCircle.append(matrix[s + l - 1][i])
            for j in range(s + l - 2, s, -1):
                self.listOneCircle.append(matrix[j][s])
            if l > 2 and c > 2:
                self.oneCircle(matrix, s + 1, l - 2, c - 2)


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        else:
            L = np.array(matrix)
            l, c = L.shape
            self.oneCircle(matrix, 0, l, c)
            return self.listOneCircle
