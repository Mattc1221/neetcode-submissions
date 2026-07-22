class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # S: O(Nlog(N)) M: O(N + M)
        return sorted(s) == sorted(t)