
class Solution:
    def bucketSortSol(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts: counts[num] = 1 + counts[num]
            else: counts[num] = 1

        print('counts', counts)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for value, count in counts.items():
            if count in buckets: buckets[count] = [value]
            else: buckets[count].append(value)

        print('buckets', buckets)
        
        top_k = []
        for i in range(len(buckets) - 1, 0, -1):

            top_k = top_k + buckets[i][:k-len(top_k)]
            if len(top_k) == k: return top_k
        return top_k

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.bucketSortSol(nums, k)