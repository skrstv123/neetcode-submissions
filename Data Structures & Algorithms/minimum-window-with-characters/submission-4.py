from collections import Counter as C, defaultdict as df
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfm = C(t)
        unq_chars = len(tfm)
        in_hand = 0
        l, r = 0, 0
        cfm = df(int)
        ansl = float('inf')
        anss = []
        while r < len(s):
            cfm[s[r]] += 1
            if s[r] in tfm and tfm[s[r]] == cfm[s[r]]:
                in_hand += 1
            if in_hand == unq_chars:
                # if r-l+1 < ansl:
                #     ansl = r-l+1
                #     anss = [l,r]
                while l<=r and in_hand == unq_chars:
                    if r-l+1 < ansl:
                        ansl = r-l+1
                        anss = [l,r]
                    cfm[s[l]] -= 1
                    if s[l] in tfm and cfm[s[l]] < tfm[s[l]]:
                        in_hand -= 1
                    l += 1
            r += 1
        return s[anss[0]: anss[1]+1] if anss else ''