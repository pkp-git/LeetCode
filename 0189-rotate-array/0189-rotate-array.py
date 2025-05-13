class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        
        cache = nums[-k:]

        for i in range(len(nums)-k-1,-1,-1):
            nums[i+k] = nums[i]
        
        for j in range(0,k):
            nums[j] = cache[j]

        print(nums)
        