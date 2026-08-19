class Solution:
    def serialize(self, s: str) -> str:
        arr = [0] * 26
        for c in s:
            i = ord(c) - ord("a")
            arr[i] += 1
        return str(arr)


    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        serialized_s1 = self.serialize(s1)
        i, j = 0, 0
        arr = [0] * 26
        # arr[ord(s2[i]) - ord("a")] = 1
        while j < len(s2):
            char_index = ord(s2[j]) - ord("a")
            arr[char_index] += 1
            if j - i + 1 == len(s1):
                print("TEST ", s2[i:j+1], str(arr), serialized_s1)
                if str(arr) == serialized_s1: 
                    return True
                arr[ord(s2[i]) - ord("a")] -= 1
                i += 1
            j += 1
        return False

        