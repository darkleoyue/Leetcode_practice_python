class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        wordDict = set(wordDict)
        memo = [1] * (len(s) + 1)

        def DSF(pos, temp):
            num = len(res)
            if pos == len(s):
                res.append(" ".join(temp))
                return
            for i in range(pos, len(s) + 1):
                if memo[i] and s[pos:i] in wordDict:
                    temp.append(s[pos:i])
                    DSF(i, temp)
                    temp.pop()
            if num == len(res):
                memo[pos] = 0
        
        DSF(0, [])
        return res
