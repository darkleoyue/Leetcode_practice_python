class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        
        for first in range(len(nums) - 2): 
            if nums[first] == nums[first - 1]: continue
            second = first + 1
            third = len(nums) - 1
            
            while second < third:
                sumThree = nums[first] + nums[second] + nums[third]

                if abs(sumThree - target) < abs(res - target):
                    res = sumThree
                
                if sumThree > target:
                    third -= 1
                elif sumThree < target:
                    second += 1
                else:
                    return target
                    
        return res
