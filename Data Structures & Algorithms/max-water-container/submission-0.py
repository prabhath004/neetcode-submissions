class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(heights)-1
        while l < r:
            width = r - l
            area = width  * min(heights[l],heights[r])
            maxarea = max(maxarea, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxarea        