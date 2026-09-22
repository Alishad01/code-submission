class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        count = 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow+=1
                nums[slow] = nums[fast]
                count+=1
            fast+=1
        return count            