class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mr = 0

        for i in range(0,len(nums)):
            val = nums[i]
            if mr < i:
                return False
            mr = max(val+i, mr)
        return True