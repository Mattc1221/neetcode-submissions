from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1

        buckets = [[]] * len(nums)
        for val, count in seen.items():
            buckets[count - 1] = buckets[count - 1] + [val]


        res = []
        for i in range(len(nums) - 1, -1, -1):
            if len(buckets[i]) != 0:
                res = res + buckets[i]
                if len(res) == k: return res
        return res

        
        