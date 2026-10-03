class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        length = k % n
        
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] =nums[r], nums[l]
                l, r = l+1, r-1
        reverse(nums, 0, n-1)
        reverse(nums, 0, length-1)
        reverse(nums, length, n-1)
