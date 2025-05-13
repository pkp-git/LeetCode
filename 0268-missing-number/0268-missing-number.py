class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) not in nums:
            return len(nums)
        
        for i in range(0,len(nums)):
            if i != nums[i]:
                return i
        
        return 