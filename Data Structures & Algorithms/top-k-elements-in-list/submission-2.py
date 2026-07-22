from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for n in nums:
            seen[n] += 1

        print(seen)

        buckets = [[]] * len(nums)
        print(buckets)
        for val, count in seen.items():
            print(val, count)
            buckets[count - 1] = buckets[count - 1] + [val]
        print(buckets)


        res = []
        for i in range(len(nums) - 1, -1, -1):
            print(i)
            if len(buckets[i]) != 0:
                res = res + buckets[i]
                if len(res) == k: return res
        return res

        
        