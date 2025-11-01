class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        maxi = len(nums)
        maxi = (maxi*(maxi+1))/2
        return int(maxi - s)