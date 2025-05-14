class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        count = [0,0,0]

        for i in nums:
            count[i]+=1

        idx = 0
        for i in range(3):
            for j in range(count[i]):
                nums[idx] = i
                idx += 1        