class Solution:
    def _solution1(self, nums: List[int], target: int) -> List[int]:
        # Solution 1: Sliding Pointers
        # C: O(n^2) M: O(1)
        for i in range(len(nums) - 1):
            for k in range (len(nums) - (i + 1)):
                j = i + k + 1
                print(i, j)
                if nums[i] + nums[j] == target: return [i, j]
        return [i, j]

    def _solution2(self, nums: List[int], target: int) -> List[int]:
        # Solution 2: Hash
        # t, [ a b c d ]
        #        j
        # 1. check in map?   
        # { t-a: i, t-b: i }
        # C: O() M: O()

        m = {}
        for j in range(len(nums)):
            if nums[j] in m:
                return [m[nums[j]], j]
            m[target - nums[j]] = j
    

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self._solution2(nums, target)
            