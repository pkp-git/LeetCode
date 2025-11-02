class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        l = len(nums)
        for i in range(0,l):
            d[nums[i]] = i
        for i in range(0,l):
            x = target - nums[i]
            if x in d:
                if d[x] != i:
                    return [d[x], i]
        return -1