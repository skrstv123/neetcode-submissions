from collections import Counter as C
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ad = C(s)
        bd = C(t)
        if ad.keys() == bd.keys():
            for k in ad.keys():
                if ad[k] != bd[k]:
                    return False
            return True
        return False