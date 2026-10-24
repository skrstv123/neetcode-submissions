class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        lp, rp = 0, len(height) - 1
        left_wall, right_wall = height[lp], height[rp]
        while lp < rp:
            if left_wall <= right_wall:
                lp += 1
                left_wall = max(left_wall, height[lp])
                total_water += (left_wall - height[lp])
            else:
                rp -= 1
                right_wall = max(right_wall, height[rp])
                total_water += (right_wall - height[rp])
                
        return total_water