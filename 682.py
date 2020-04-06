class Solution:
    def calPoints(self, ops: List[str]) -> int:
        num = []
        
        for i in ops:
            if i.isdigit():
                num.append(int(i))
            elif i.lstrip('-').isdigit():
                num.append(int(i))
            elif i == 'C':
                num.pop()
            elif i == 'D':
                num.append(num[-1]*2)
            elif i == '+':
                num.append(num[-1] + num[-2])
        
        return sum(num)
