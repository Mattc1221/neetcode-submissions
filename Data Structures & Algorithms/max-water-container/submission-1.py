class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        area = (j-i) * max(heights[i], height[j])
        '''
        max_area = -1
        for i in range(len(heights)):
            j = i + 1
            while j < len(heights):
                area = (j-i) * min(heights[i], heights[j])
                max_area = max(max_area, area)
                j += 1
        return max_area

