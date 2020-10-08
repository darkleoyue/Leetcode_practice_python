class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        m = int(len(s) / 2)
        n = 0 if len(s) % 2 else 1
        for i in range(m):
            temp = s[i]
            s[i] = s[2 * m - n - i]
            s[2 * m - n - i] = temp
            
            
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s.reverse()
