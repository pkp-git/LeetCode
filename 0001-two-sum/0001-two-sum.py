class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            d[nums[i]] = i
        for i in range(0,len(nums)):
            x = target - nums[i]
            if x in d:
                if i != d[x]:
                    return [d[x],i]
        return -1