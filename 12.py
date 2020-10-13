class Solution:

    def addNum(self, index, char1, char2, char3, res):
        if index < 5:
            if index == 4:
                res = res + char1 + char2
            else:
                res = res + char1 * index
        
        else:
            if index == 9:
                res = res + char1 + char3
            else:
                res = res + char2 + char1 * (index - 5)
        
        return res

    def intToRoman(self, num: int) -> str:
        forth = (num // 1000) % 10
        third = (num // 100) % 10
        second = (num // 10) % 10
        first = num % 10
        
        res = "M" * forth
        res = self.addNum(third, 'C', 'D', 'M', res)
        res = self.addNum(second, 'X', 'L', 'C', res)
        res = self.addNum(first, 'I', 'V', 'X', res)

        return res
        
