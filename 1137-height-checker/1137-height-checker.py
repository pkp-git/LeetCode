class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sorte = sorted(heights)
        for i in range(0,len(heights)):
            if sorte[i] != heights[i]:
                count = count + 1
        return count