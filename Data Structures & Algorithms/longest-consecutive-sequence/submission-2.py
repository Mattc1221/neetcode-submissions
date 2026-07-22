class Solution:
    def sol1(self, nums: List[int]) -> int:
        max_count = 0
        count = 1
        prev = None
        nums = sorted(nums)
        for i in range(len(nums)):
            cur = nums[i]
            if prev is not None:
                diff = cur - prev
                if (diff > 1): count = 1
                elif diff == 1: count += 1
            max_count = max(max_count, count)
            prev = cur
        return max_count

        
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.sol1(nums)


            

        