from collections import Counter as C
import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorted_by_freq = sorted(C(nums).items(), key = lambda x: -x[1])
        # return list(map(lambda x: x[0], sorted_by_freq))[:k]
        counts = C(nums)
        hp = []
        for ki in counts.keys():
            hq.heappush(hp, (counts[ki], ki))
            if len(hp) > k:
                hq.heappop(hp)
        return [hq.heappop(hp)[1] for i in range(k)]