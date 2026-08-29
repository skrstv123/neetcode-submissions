class Solution:
    def search(self, arr: List[int], target: int) -> int:

        def isrotated(arr: List[int]) -> bool:
            return arr[0] > arr[-1]

        def bs(l: int, r: int, arr: List[int], e: int) -> int:
            while l<=r:
                m = (l+r) // 2
                em = arr[m]
                if em == e:
                    return m
                if em < e:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        def findpivot(arr: List[int]):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l+r) // 2
                em = arr[m]
                if em >= arr[0]:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        if isrotated(arr):
            m = findpivot(arr)
            return max(bs(0, m-1, arr, target), bs(m, len(arr) - 1, arr, target))
        else:
            return bs(0, len(arr)-1, arr, target)


        