class Solution:

    def square(self, x):
        return x ** 2
    
    def sortedSquares(self, A: List[int]) -> List[int]:
        squaredList = map(self.square, A)
        return sorted(squaredList)
