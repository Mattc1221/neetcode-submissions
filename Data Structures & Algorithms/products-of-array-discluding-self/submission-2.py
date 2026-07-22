class Solution:
    def sol1(self, nums: List[int]) -> List[int]:
        """
        C: O(n)
        M: O(n)
        """
        res = [0] * len(nums)
        p = 1
        has_zero = False
        for i in range(len(nums)):
            n = nums[i]
            if n == 0: 
                if has_zero: return res
                has_zero = True
            else: p = n * p

        for i in range(len(nums)):
            n = nums[i]
            if n == 0: res[i] = p
            elif has_zero: res[i] = 0
            else:
                res[i] = int(p / n)

        return res


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.sol1(nums)



            
