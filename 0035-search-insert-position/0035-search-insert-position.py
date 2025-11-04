class Solution:
    def searchInsert(self, nums: List[int], tgt: int) -> int:
        low = 0
        high = len(nums)-1
        pv = 0

        def BS(low, high, pv):
            if low > high:
                return pv

            mid = (low+high)//2

            if nums[mid] == tgt:
                return mid
            
            if nums[mid] < tgt:
                return BS(mid+1, high, mid+1)
            else:
                return BS(low, mid-1, mid)
        return BS(low, high, pv)