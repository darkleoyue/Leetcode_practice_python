class Solution:
    def isValid(self, s: str) -> bool:
        tmp = [0]
        
        for i in s:
            if i == '(':
                tmp.append(1)
            elif i == '[':
                tmp.append(2)
            elif i == '{':
                tmp.append(3)
            elif i == ')':
                if tmp.pop() == 1:
                    continue
                else:
                    return False
            elif i == ']':
                if tmp.pop() == 2:
                    continue
                else:
                    return False
            elif i == '}':
                if tmp.pop() == 3:
                    continue
                else:
                    return False
                
        if tmp == [0]:
            return True
        else:
            return False
