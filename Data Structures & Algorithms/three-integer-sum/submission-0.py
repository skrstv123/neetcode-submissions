class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] ==  nums[i-1]:
                continue
            x, y = i + 1, n - 1
            while x < y:
                sm = nums[i] + nums[x] + nums[y]
                if sm == 0:
                    ans.append([nums[i], nums[x], nums[y]])
                    while x + 1 < y and nums[x + 1] == nums[x]:
                        x += 1
                    while y - 1 > x and nums[y - 1] == nums[y]:
                        y -= 1
                if sm < 0:
                    x += 1
                else:
                    y -= 1
        return ans

