class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = set(nums)
        count = 1
        for n in ans:
            if n==count:
                count+=1
        return count