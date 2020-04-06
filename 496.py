class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        def find_next(a, ls):
            for i, num in enumerate(ls):
                if num == a:
                    for j in ls[i:]:
                        if j > a:
                            return j
                    return -1

        for i in nums1:
            b = find_next(i,nums2)
            result.append(b)
        
        return result
