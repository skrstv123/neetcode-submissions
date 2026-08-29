from collections import Counter as C
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_by_freq = sorted(C(nums).items(), key = lambda x: -x[1])
        return list(map(lambda x: x[0], sorted_by_freq))[:k]