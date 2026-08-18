class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        numbers
            sorted in non-decreasing order

        [ a, b, c, d, e ]
             i     j
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target: break
            if total < target: i += 1
            else: j -= 1

        return [i+1, j+1]