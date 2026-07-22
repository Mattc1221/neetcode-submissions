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


    def sol2(self, nums: List[int]) -> List[int]:
        prefix, postfix, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)
        for i in range(len(nums)):
            prefix[i] = nums[i] * prefix[i-1]


            j = len(nums) - 1 - i
            post = 1 if j+1 >= len(nums) else postfix[j+1]
            postfix[j] = nums[j] * post

        print(prefix, postfix)
        
        for i in range(len(nums)):
            pre =  1 if i-1 < 0 else prefix[i-1]
            post =  1 if i+1 >= len(nums) else postfix[i+1]
            res[i] = pre * post
        return res
            




    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.sol2(nums)



            
