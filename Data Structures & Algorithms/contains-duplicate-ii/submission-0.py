class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashy = {}
        for i in range(len(nums)):
            if nums[i] not in hashy:
                hashy[nums[i]]=i
            else:
                if abs(hashy[nums[i]] - i) <=k:
                    return True
                else:
                    return False
        return False