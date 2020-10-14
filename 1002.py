class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return reduce(lambda x, y : x & y, map(collections.Counter, A)).elements()
