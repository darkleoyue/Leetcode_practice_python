class Solution:
    
    def dfs(self, subset, index, nums, cur):
        if index >= len(nums):
            subset.append(cur)
            return
        temp = cur.copy()
        self.dfs(subset, index + 1, nums, temp)
        cur.append(nums[index])
        self.dfs(subset, index + 1, nums, cur)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        self.dfs(subset, 0, nums, [])
        return subset
