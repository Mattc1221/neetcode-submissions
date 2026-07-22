class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            target = nums[i] * -1
            j, k = i + 1, len(nums) - 1
            while j < k:
                val = nums[j] + nums[k]
                if val < target: 
                    j += 1
                elif val > target: 
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:  # skip duplicate j
                        j += 1
        return res





