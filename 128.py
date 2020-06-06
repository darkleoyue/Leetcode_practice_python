class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        else:
            num_len = {}
            max_len = 1
            for num in nums:
                if num not in num_len:
                    left = num_len[num - 1] if num - 1 in num_len else 0
                    right = num_len[num + 1] if num + 1 in num_len else 0
                    num_len[num] = left + right + 1
                    num_len[num - left] = num_len[num]
                    num_len[num + right] = num_len[num]
                    max_len = max(max_len, num_len[num])
            return max_len
