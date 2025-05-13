class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = 0

        for i in nums:
            if i != 0:
                count += 1
                maxi = max(maxi,count)

            else:
                maxi = max(maxi,count)
                count = 0

        return maxi