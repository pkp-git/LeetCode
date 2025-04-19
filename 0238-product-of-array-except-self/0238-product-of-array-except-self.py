class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        pp = [1]*n
        sp = [1]*n

        for i in range(1,n):
            pp[i] = nums[i-1] * pp[i-1]
        
        for j in range(n-2, -1, -1):
            sp[j] = nums[j+1] * sp[j+1]

        for i in range(n):
            nums[i] = pp[i]*sp[i]

        return nums