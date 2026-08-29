from collections import Counter as C, defaultdict as df
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = C(t)
        n = len(s)
        rsc = df(int)

        i = 0
        formed = 0
        minl, optimali = float('inf'), -1
        req = len(tc)
        for j in range(n):
            c = s[j]
            rsc[c] += 1

            if c in tc and rsc[c] == tc[c]:
                formed += 1
                # if formed == req:
                #     cl = j - i + 1
                #     if cl < minl:
                #         minl = cl
                #         optimali = i
            
            while i <= j and formed == req:
                cl = j - i + 1
                if cl < minl:
                    minl = cl
                    optimali = i

                ci = s[i]
                rsc[ci] -= 1
                i += 1
                if ci in tc and rsc[ci] < tc[ci]:
                    formed -= 1

        return '' if optimali == -1 else s[optimali: optimali + minl]

