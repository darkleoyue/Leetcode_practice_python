class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = ""
        temp = ""
        for i in s:
            if i not in temp:
                temp += i
            else:
                temp = temp[temp.index(i) + 1 :]
                temp += i
            if len(temp) > len(ans):
                ans = temp

        return len(ans)
