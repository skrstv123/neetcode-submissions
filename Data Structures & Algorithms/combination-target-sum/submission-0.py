class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def bt(i, curr, rem):
            if rem == 0:
                res.append(list(curr))
                return 
            for j in range(i, len(nums)):
                if nums[j] > rem:
                    continue
                curr.append(nums[j])
                bt(j, curr, rem - nums[j])
                curr.pop()
        bt(0, [], target)
        return res