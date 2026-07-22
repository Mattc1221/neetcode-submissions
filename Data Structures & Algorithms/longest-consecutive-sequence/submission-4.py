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

    def sol2(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        seen = dict()
        for n in nums:
            if n not in seen:
                seen[n] = {n}
                if (n - 1) in seen:
                    seen[n-1].update(seen[n])
                    seen[n] = seen[n-1]
                if (n + 1) in seen:
                    seen[n+1].update(seen[n])
                    seen[n] = seen[n+1]
                if (n+1) in seen and (n-1) in seen:
                    seen[n-1].update(seen[n+1])
                    seen[n+1] = seen[n-1]
        

        return max([len(arr) for arr in seen.values()])
                



    def longestConsecutive(self, nums: List[int]) -> int:
        return self.sol2(nums)


            

        