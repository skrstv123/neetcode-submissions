from collections import Counter as C, defaultdict as dfd
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dfd(list)
        for string in strs:
            groups[frozenset(C(string).items())].append(string)
        return list(groups.values())
        