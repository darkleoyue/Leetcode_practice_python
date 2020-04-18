class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums == []:
            return -1
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == target:
                    return m
            elif nums[l] <= nums[m]:
                if nums[m] > target and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1    
            elif nums[m] <= nums[r]:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1   

            if l == r and nums[l] != target:
                return -1
        return -1
