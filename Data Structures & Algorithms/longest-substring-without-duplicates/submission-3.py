class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        n = len(s)
        i = 0
        ans = 0
        for j in range(n):
            if s[j] not in last_pos:
                pass
            elif last_pos[s[j]] >= i:
                i = last_pos[s[j]] + 1
            last_pos[s[j]] = j
            ans = max(ans, j-i+1)
        return ans
            