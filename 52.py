class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        def DFS(i, col, dia0, dia1):
            if i == n:
                nonlocal res
                res += 1
                return
            for j in range(n):
                if j not in col and j + i not in dia0 and j - i not in dia1:
                    DFS(i + 1, col + [j], dia0 + [j + i], dia1 + [j - i])
        DFS(0, [], [], [])
        return res
