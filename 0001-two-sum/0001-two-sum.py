class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numidx = [(num, i) for i, num in enumerate(nums)]
        numidx.sort(key=lambda x: x[0])
        
        i = 0
        j = len(numidx) - 1
        
        while i < j:
            total = numidx[i][0] + numidx[j][0]
            if total == target:
                return [numidx[i][1], numidx[j][1]]
            elif total < target:
                i += 1
            else:
                j -= 1
        
        return []
