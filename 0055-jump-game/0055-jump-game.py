class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mr = 0

        for i in range(0,len(nums)):
            val = int(nums[i])
            if mr < i:
                return False
            mr = max(i+val,mr)
        return True