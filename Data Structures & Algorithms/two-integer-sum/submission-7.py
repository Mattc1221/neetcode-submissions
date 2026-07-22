class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1: Sliding Pointers
        # [ 5 5 ]
        #   i j
        # k = j - i -> j = k + i
        # C: O(n^2) M: O(1)

        for i in range(len(nums) - 1):
            for k in range (len(nums) - (i + 1)):
                j = i + k + 1
                print(i, j)
                if nums[i] + nums[j] == target: return [i, j]
        return [i, j]
            