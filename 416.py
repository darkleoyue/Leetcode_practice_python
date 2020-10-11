class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2

        dp = [[False] * (target + 1) for _ in range(n)]
        dp[0][0] = True
        for i in range(1, target + 1):
            if i == nums[0]:
                dp[0][i] = True
                break
        
        for j in range(1, n):
            for i in range(target + 1):
                if i >= nums[j]:
                    dp[j][i] = dp[j - 1][i] or dp[j - 1][i - nums[j]]
                else:
                    dp[j][i] = dp[j - 1][i]
        
        return dp[-1][-1]
