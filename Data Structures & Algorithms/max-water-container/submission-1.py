class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_height = 0
        while l < r:
            if heights[r] > heights[l]:
                l+=1
                max_height = max(max_height, abs(r-l) * min(heights[r], heights[l]))
            elif heights[l] > heights[r]:
                r-=1 
                max_height = max(max_height, abs(r-l) * min(heights[r], heights[l]))
            else:
                max_height= max(max_height, abs(r-l) * min(heights[r], heights[l]))
                l+=1
                r-=1
            print(max_height)
        return max_height