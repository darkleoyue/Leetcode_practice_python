class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:

        i = 0
        j = 0
        n = len(name)
        m = len(typed)
        while j < m:
            if i < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        
        return i == n
