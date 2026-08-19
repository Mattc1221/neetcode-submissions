class Solution:
    def serialize(self, s: str) -> str:
        arr = [0] * 26
        for c in s:
            i = ord(c) - ord("a")
            arr[i] += 1

        print("SERIALIZED ", s, " to ", str(arr))
        return str(arr)


    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        serialized_s1 = self.serialize(s1)
        i, j = 0, len(s1) - 1
        while j < len(s2):
            substring = s2[i:j+1]
            if serialized_s1 == self.serialize(substring): return True
            i += 1
            j += 1
        return False

        