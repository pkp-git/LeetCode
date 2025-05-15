class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for i in nums: 
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        nums = []
        
        for i in range(0,len(pos)):
            nums.append(pos[i])
            nums.append(neg[i])
        
        return nums