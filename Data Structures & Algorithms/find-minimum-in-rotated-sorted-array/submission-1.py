class Solution:
    def findMin(self, arr: List[int]) -> int:
        
        def isrotated(arr):
            return arr[0] > arr[-1]

        def bs(l, r, arr, e):
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
        
        def findpivot(arr):
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
            return arr[m]
        else:
            return arr[0]


