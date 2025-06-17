class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxheight = 0
        localheight = 0

        for i in s:
            if i == '(':
                stack.append(i)
                localheight += 1
            elif i == ')':
                stack.pop()
                localheight -= 1
            maxheight = max(maxheight,localheight)
        return maxheight
