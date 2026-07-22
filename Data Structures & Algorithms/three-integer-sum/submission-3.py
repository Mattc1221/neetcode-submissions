class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums) - 2):
            target = nums[i] * -1
            j, k = i + 1, len(nums) - 1
            while j < k:
                val = nums[j] + nums[k]
                if val < target: 
                    j += 1
                elif val > target: 
                    k -= 1
                else:
                    if i < j: 
                        res.add((nums[i], nums[j], nums[k]))
                    elif i < k:
                        res.add((nums[j], nums[i], nums[k]))
                    else:
                        res.add((nums[j], nums[k], nums[i]))
                    j += 1
                    k -= 1
        return list(res)





