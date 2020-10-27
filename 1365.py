class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        elif len(nums) == 1:
            return [0]
        
        n = len(nums)
        res = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    res[i] += 1
                elif nums[i] < nums[j]:
                    res[j] += 1
        
        return res
