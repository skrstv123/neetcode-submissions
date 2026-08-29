import heapq as hq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capprof = sorted(zip(capital, profits), key = lambda x: x[0])
        mheap = []
        caplen = len(capprof)
        curridx = 0
        currcap = w

        for i in range(k):
            while curridx < caplen and capprof[curridx][0] <= currcap:
                hq.heappush(mheap, -capprof[curridx][1])
                curridx += 1
            if mheap:
                currcap += -hq.heappop(mheap)
            else:
                break
        return currcap

        