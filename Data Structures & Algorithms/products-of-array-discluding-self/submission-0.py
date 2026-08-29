class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prfp = []
        for i in nums:
            prfp.append(prfp[-1] * i if prfp else i) 

        sufp = []
        for i in range(len(nums) - 1, -1, -1):
            e = nums[i]
            sufp.append(e * sufp[-1] if sufp else e)

        sufp.reverse()

        ans = []
        for i in range(len(nums)):
            ppes = prfp[i-1] if i > 0 else 1
            spes = sufp[i+1] if i+1 < len(nums) else 1
            ans.append(ppes * spes)
        return ans
        

        