class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        
        for index, num in enumerate(nums):
            
            other = target - num
            
            if other in tmp:
                return [tmp[other], index]
            else:
                tmp[num] = index
                
        return []
