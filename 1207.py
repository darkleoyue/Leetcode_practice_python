class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dict_alpha = {}
        for i in arr:
            if i in dict_alpha.keys():
                dict_alpha[i] += 1
            else:
                dict_alpha[i] = 1
        
        values = []
        for i in dict_alpha.values():
            values.append(i)

        set_val = set(values)
        n = len(values)
        m = len(set_val)

        return n == m
