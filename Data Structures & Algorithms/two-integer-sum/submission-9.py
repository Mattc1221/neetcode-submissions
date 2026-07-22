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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self._solution1(nums, target)
            