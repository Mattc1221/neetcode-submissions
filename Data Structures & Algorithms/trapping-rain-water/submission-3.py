class Solution:
    def trap(self, height: List[int]) -> int:
        """
         0 1 2 3 4 5 6 7 8 9
        [0,2,0,3,1,0,1,3,2,1]

        v = 0
        l = 1
        r = 9
        maxL = 0
        maxR = 1

        """
        # At each position, how much water can that position hold?
        # This is bound by Min(nearest left peak, nearest right peak)
        # Calc = min(L, R) - h_i
        

        l, r = 0, len(height) -1
        maxL, maxR = height[0], height[r]
        v = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(height[l], maxL)
                v += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                v += maxR - height[r]
        return v
