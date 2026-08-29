class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxarea = 0
        i, j = 0, len(h) - 1

        while i < j:
            area = min(h[i], h[j]) * (j-i)
            maxarea = max(area, maxarea)

            if h[i] < h[j]:
                i += 1
            else:
                j -= 1
        return maxarea
        