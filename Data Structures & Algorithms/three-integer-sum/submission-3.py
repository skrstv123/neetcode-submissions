class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_set = []
        nums.sort()
        # l, r = 0, len(nums) - 1
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if not s:
                    ans_set.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    continue
                if s > 0:
                    r -= 1
                else:
                    l += 1
                
        return ans_set
                