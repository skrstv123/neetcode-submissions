from collections import defaultdict as dfd
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        item_indices = dfd(list)
        for i,e in enumerate(nums):
            item_indices[e].append(i)
            if target - e in item_indices:
                if (e == (target - e)):
                    if len(item_indices[e]) > 1:
                        return item_indices[e][:2]
                    else:
                        continue
                else:
                    return [item_indices[target - e][0], item_indices[e][0]]
                
        
