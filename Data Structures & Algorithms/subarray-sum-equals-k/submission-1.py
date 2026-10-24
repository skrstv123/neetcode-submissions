from collections import defaultdict as df
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psf = df(int)
        psf[0] = 1 # empty subarray
        ans = 0

        n = len(nums)
        s = 0
        for i in range(n):
            s += nums[i]
            psf[s] += 1
            ans += psf[s-k]
            
            if s-k == s:
                ans -= 1

        return ans
        