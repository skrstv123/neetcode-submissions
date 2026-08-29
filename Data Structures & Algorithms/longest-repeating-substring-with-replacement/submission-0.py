from collections import defaultdict as df
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cfrq = df(int)
        n = len(s)
        i = 0
        max_frq = 0
        ans = 0
        for j in range(n):
            cfrq[s[j]] += 1
            max_frq = max(max_frq, cfrq[s[j]])
            if (j - i + 1) - max_frq > k:
                cfrq[s[i]] -= 1
                i += 1 
            ans = max(ans, j-i+1)
        return ans
