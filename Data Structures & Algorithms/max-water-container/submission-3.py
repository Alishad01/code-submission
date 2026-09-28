class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_height = 0
        while l < r:
            max_height= max(max_height, abs(r-l) * min(heights[r], heights[l]))
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return max_height