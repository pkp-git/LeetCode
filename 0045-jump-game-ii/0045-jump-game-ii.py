class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        fp = 0
        for i in range(0,len(nums)-1):
            fp = max(fp, i+nums[i])

            if i == current_end: 
                jumps = jumps + 1
                current_end = fp
        
        return jumps