class Solution:
    def longestMountain(self, A: List[int]) -> int:
        
        n = len(A)
        if n < 3:
            return 0
        dp1 = [1] * n
        dp2 = [1] * n

        for i in range(1, n):
            if A[i] > A[i - 1]:
                dp1[i] += dp1[i - 1]
        
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                dp2[i] += dp2[i + 1]

        res = 0
        for i in range(1, n - 1):
            if dp1[i] > 1 and dp2[i] > 1:
                cur = dp1[i] + dp2[i] - 1
                res = max(cur, res)
        
        return res
