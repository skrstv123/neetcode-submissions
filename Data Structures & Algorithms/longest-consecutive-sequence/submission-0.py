class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unq_elms = set(nums)
        ans = 0
        for i in unq_elms:
            cur = i
            if cur - 1 not in unq_elms:
                cnt = 1
                while cur + 1 in unq_elms:
                    cur += 1
                    cnt += 1
                ans = max(ans, cnt)
        return ans



        
