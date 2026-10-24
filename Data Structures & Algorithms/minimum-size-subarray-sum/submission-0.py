class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cs = 0
        l = r = 0
        n = len(nums)
        ans = float('inf')
        while r < n:
            cs += nums[r]
            while l<=r and cs>=target:
                ans = min(ans, r-l+1)
                cs -= nums[l]
                l += 1
            r += 1
        return ans if ans != float('inf') else 0
        