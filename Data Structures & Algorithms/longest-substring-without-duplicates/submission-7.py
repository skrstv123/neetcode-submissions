class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        firstpos = {}
        l = r = ans = 0
        while r < len(s):
            if s[r] not in firstpos or firstpos[s[r]] < l:
                firstpos[s[r]] = r
                r += 1
                ans = max(ans, r-l)
            else:
                l = firstpos[s[r]] + 1
                firstpos[s[r]] = r
                # firstpos = {s:i for s,i in firstpos.items() if i>=l}
                r += 1
        return ans
        