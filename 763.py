class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        max_index = {item : index for index, item in enumerate(S)}
        start, end = 0, 0
        res = []

        for index, item in enumerate(S):
            end = max(end, max_index[item])
            if end == index:
                res.append(end - start + 1)
                start = end + 1
        
        return res
