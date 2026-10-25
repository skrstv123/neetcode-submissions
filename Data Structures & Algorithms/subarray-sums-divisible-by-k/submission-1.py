from collections import defaultdict as df
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        modf = df(int)
        modf[0] = 1
        s = 0
        ans = 0
        for i in nums:
            s += i
            ans += modf[s%k]
            # increment after using
            # mC2 is sum of natural numbers upto m-1 not m
            modf[s%k] += 1
        
        # for v in modf.values():
        #     ans += (v*(v-1))//2
        return ans